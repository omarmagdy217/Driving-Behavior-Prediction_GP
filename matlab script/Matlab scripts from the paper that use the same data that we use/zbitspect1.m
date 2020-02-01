%OPERATOR STATE ANALYZER
% clear,clc,close all

valthr=0.20;            %fraction of validation samples


%% OPTIONS
frqthr=18;              %high frequency threshold (20 Hz)
df=1.0;                 %average power into bands
TT=15;                  %spectrogram window, sec
dT=1;                   %spectrogram T-step, sec
TA=ceil(15/dT);          %average power over time (15 sec)

%% LOAD DATA
fprintf('Loading data\n');
load mc_eegkaydi1.mat
O{1}=o;

load mc_eegkaydi2.mat
O{2}=o;

load mc_eegkaydi3.mat
O{3}=o;

load mc_eegkaydi4.mat
O{4}=o;

load mc_eegkaydi5.mat
O{5}=o;

%(!) load eegkaydi.mat FIRST (!)
% EEG data is o.data(:,4:17)

fprintf('Calculating spectrograms\n');
nn=length(O);
P_full=cell(1,nn);
T=cell(1,nn);
for cnt=1:5
  eegdata=O{cnt}.data(:,4:17);
  
  % valid channels
  ch=[2,3,6,7,8,9,14];
  
  vdata=eegdata;  
  
  % stack spectrograms from all data channels
  P_full{cnt}=[];
  
  for k=ch
    % S is the Fourier transform (amplitude + phase, complex value);
    % F is set of frequencies for S,P (vertical dim);
    % T is set of times for S,P (horizontal dim);
    % P is power spectra (amplitude^2)
    % TT is the length of the window on which to calculate stfft    
    [S,f,T{cnt},p] = spectrogram(vdata(:,k),...
        blackman(TT*128),TT*128-dT*128,8*128,128);
    
    %correct for T's being centers of respective windows
    T{cnt}=T{cnt}+TT/2;
      
    %limit frequencies
    p=p(f>0 & f<=frqthr,:);
    f=f(f>0 & f<=frqthr);   
    
    %mean power per df frequency-band (true power)
    if(df>0)
      pb=[];
      for ff=0:df:frqthr-df
        pb=cat(1,pb,mean(p(f>ff & f<=ff+df,:),1));
      end  
      p=pb;
    end

    p=10*log10(p);
    p=max(-100,p);    
    
    dk=size(p,1);
        
    %stack spectrograms
    P_full{cnt}=cat(1,P_full{cnt},p);
    
    % convert time to mins
    T{cnt}=T{cnt}/60;
  end
end

save temp P_full T
load temp

%% TRAIN
% load temp

t_active=9;      % end of active phase, min !set from real data!
t_unfocused=19;   % end of unfocused phase, min !set from real data!
t_sleep_start=21; % start of sleep alpha waves, min !set from data!
t_sleep_end=30;   % end of sleep alpha waves, min !set from data!

%% apply SVM on collated data


%collate data
PP=[];
TT=[];
ID=[];
for cnt=1:5
  PP=cat(2,PP,P_full{cnt});
  TT=cat(2,TT,T{cnt});
  ID=cat(2,ID,repmat(cnt,1,size(T{cnt},2)));
end

%average over time 
if(TA>0)
   PP=filter(1/TA*ones(1,TA),1,PP,[],2); 
end

%limit data range
tidx=(TT>1 & TT<t_active) | (TT>t_active+2 & TT<t_unfocused) ...
  | (TT>t_sleep_start & TT<t_sleep_end);
PP_train=PP(:,tidx);
TT=TT(tidx);
ID=ID(tidx);

%svmtrain
labels=zeros(size(PP_train,2),1);
labels(TT>1 & TT<t_active)=1;
labels(TT>t_active+2 & TT<t_unfocused)=2;
labels(TT>t_sleep_start & TT<t_sleep_end)=3;
train_sel=rand(size(labels))>valthr;

fprintf('Total examples %i\n',sum(labels>0));
fprintf('Train %i\n',sum(train_sel));
fprintf('Validation %i\n',sum(~train_sel));
fprintf('Features %i\n',size(PP_train,1));

fprintf('Applying SVM, all experiments\n');

SVMStruct=cell(1,3);
options=svmsmoset('MaxIter',20000000);
for i=1:3
  SVMStruct{i} = svmtrain(PP_train(:,train_sel)',...
      labels(train_sel)==i,'Method','LS');      
      %labels_train(train_sel)==i,'Method','SMO','SMO_OPTS',options);
end

%validation
Group=zeros(sum(~train_sel),3);
for i=1:3
  Group(:,i)=svmclassify(SVMStruct{i},PP_train(:,~train_sel)');
end
[garbage,GroupT]=max(Group,[],2);
GroupT(sum(Group,2)>1)=0;         %remove double hits

labels_chk=labels(~train_sel);
for cnt=1:5
  trange=labels_chk>0 & ID(~train_sel)'==cnt;
  percentageCorrect = ...
    (sum( labels_chk(trange)==GroupT(trange) )/ sum(trange))*100;
  fprintf('Validation correct, experiment #%i: %g\n',cnt,percentageCorrect);
end

trange=labels_chk>0;
percentageCorrect = ...
  (sum( labels_chk(trange)==GroupT(trange) )/ sum(trange))*100;
fprintf('Validation correct, average: %g\n',percentageCorrect);

%% Apply SVM on separate data
fprintf('Applying SVM, one experiment\n');
fprintf('Features %i\n',size(PP_train,1));

pf=zeros(1,5);
for cnt=1:5
  train_sel_loc=train_sel & ID'==cnt;
  test_sel_loc=~train_sel & ID'==cnt;
  
  fprintf('Experiment %i: train %i,',cnt,sum(train_sel_loc));
  fprintf('validation %i\n',sum(test_sel_loc));
  
  
  SVMStruct=cell(1,3);
  options=svmsmoset('MaxIter',20000000);
  for i=1:3
    SVMStruct{i} = svmtrain(PP_train(:,train_sel_loc)',...
      labels(train_sel_loc)==i,'Method','LS');
    %labels_train(train_sel)==i,'Method','SMO','SMO_OPTS',options);
  end
  
  %validation
  Group=zeros(sum(test_sel_loc),3);
  for i=1:3
    Group(:,i)=svmclassify(SVMStruct{i},PP_train(:,test_sel_loc)');
  end
  [garbage,GroupT]=max(Group,[],2);
  GroupT(sum(Group,2)>1)=0;         %remove double hits
  
  labels_chk=labels(test_sel_loc);
  trange=labels_chk>0;
  percentageCorrect = ...
    (sum( labels_chk(trange)==GroupT(trange) )/ sum(trange))*100;  
  pf(cnt)=percentageCorrect;
end

for cnt=1:5
  fprintf('Validation correct, experiment #%i: %g\n',cnt,pf(cnt));
end
fprintf('Validation correct, average: %g\n',mean(pf));




