%analysis, prepare features

%% PARAMETERS
val_thr=0.20;            %fraction of samples used for validation
frq_thr=18;              %high frequency cutoff
df=0.5;                 %power spectrum bin width, Hz
TT=15;                  %STFT window, sec
dT=1;                   %STFT T-step, sec
TA=ceil(15/dT);         %running average (for 15 sec)
data='/data/Grive/TRAIN-DATA/'; %data directory

%% LOAD DATA
fprintf('Loading data\n');
files=dir([data,'*',subject,'*']);
nn=length(files);
O=cell(1,nn);
for i=1:nn
    fname=[data,'//',files(i).name];
    fprintf(' loading %s',fname);
    if ~include(i)
        fprintf(' excluded\n');
        continue;
    else
        fprintf('\n');
        load(fname)
        O{i}=o;
    end
end

%note that the actual EEG data in Emotiv is in o.data(:,4:17)

%% EXTRACT FEATURES
fprintf('Calculating STFT\n');

P_full=cell(1,nn);      %power spectra/spectrogram
T=cell(1,nn);           %corresponding time points
for cnt=1:nn
    if isempty(O{cnt})
        continue;
    end
    
    %collect spectrograms from all channels
    P_full{cnt}=[];
    
    %connected leads
    ch=[2,3,6,7,8,9,14];
    
    eegdata=O{cnt}.data(:,4:17);
    vdata=eegdata;
    
    for k=ch
        % S is the Fourier transform (amplitude + phase, complex value);
        % F is set of frequencies for S,P (vertical dim);
        % T is set of times for S,P (horizontal dim);
        % P is power spectra (amplitude^2)
        % TT is the length of the window on which to calculate stfft
        % 128 Hz is sampling frequency in emotiv
        [S,f,t,p] = spectrogram(vdata(:,k),...
            blackman(TT*128),TT*128-dT*128,8*128,128);
        
        %correct for T's calculated in spectrogram being the centers
        %of the respective window time-intervals; we want T's being
        %the end-points of the respective time-intervals
        t=t+TT/2;
        
        %convert time to mins
        t=t/60;
        
        %limit the frequencies to 0..frq_thr
        p=p(f>0 & f<=frq_thr,:);
        f=f(f>0 & f<=frq_thr);
        
        %bin power to df-frequency bins
        pb=[];
        for ff=0:df:frq_thr-df
            pb=cat(1,pb,mean(p(f>ff & f<=ff+df,:),1));
        end
        p=pb;
        
        %db scale for powers
        p=10*log10(p);
        %zeros in p produce -Inf which breaks everything, so limit at -100
        p=max(-100,p);
        
        %the 1st dimension of p (number of frequency values)
        dk=size(p,1);
        
        %running average smoothing
        p=filter(1/TA*ones(1,TA),1,p,[],2);
        
        %save the result
        P_full{cnt}=cat(1,P_full{cnt},p);
        T{cnt}=t;
    end
end

%% COLLATE DATA
t_active=9;       % end of active phase, min
t_unfocused=19;   % end of unfocused phase, min
t_sleep_start=21; % start of drowsy phase, min
t_sleep_end=30;   % end of drowsy phase, min

%collate all data
PP=[];            % PSD data
TT=[];            % time data
ID=[];            % dataset ID
for cnt=1:nn
    PP=cat(2,PP,P_full{cnt});
    TT=cat(2,TT,T{cnt});
    ID=cat(2,ID,repmat(cnt,1,size(T{cnt},2)));
end

%show power spectra, for visual inspection
figure,imagesc(PP)

%limit data to known time range
tidx=(TT>1 & TT<t_active) | (TT>t_active+2 & TT<t_unfocused) ...
    | (TT>t_sleep_start & TT<t_sleep_end);
PP_train=PP(:,tidx);
TT=TT(tidx);
ID=ID(tidx);

%train SVM
labels=zeros(size(PP_train,2),1);
labels(TT>1 & TT<t_active)=1;
labels(TT>t_active+2 & TT<t_unfocused)=2;
labels(TT>t_sleep_start & TT<t_sleep_end)=3;

%training-validation split
train_sel=rand(size(labels))>val_thr;

%print some info
fprintf('Total samples %i\n',sum(labels>0));
fprintf('Train samples %i\n',sum(train_sel));
fprintf('Validation samples %i\n',sum(~train_sel));
fprintf('Total features %i\n',size(PP_train,1));