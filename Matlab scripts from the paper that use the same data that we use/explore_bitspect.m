%OPERATOR STATE ANALYZER
clear,clc,close all

valthr=0.33;            %fraction of validation samples


%% OPTIONS
frqthr=35;              %high frequency threshold
tt=30;                  %spectrogram window
dT=1;                   %spectrogram T-step, sec
df=1;                   %average power into [df Hz]-bands {try somethng}

ntrain=[1,2,3,4];         %try different splits of train/test datasets
ntest=[5];


%% LOAD DATA
load eegkaydi26_GE.mat
O{1}=o;

load eegkaydi27_GE.mat
O{2}=o;

load eegkaydi28_GE.mat
O{3}=o;

load eegkaydi29_GE.mat
O{4}=o;

load eegkaydi37_GE.mat
O{5}=o;

%(!) load eegkaydi.mat FIRST (!)
% EEG data is o.data(:,4:17)

dk=0;
nn=length(O);
P=cell(1,nn);
T=cell(1,nn);
for cnt=union(ntrain,ntest)
  eegdata=O{cnt}.data(:,4:17);
  
  % valid channels
  ch=[2,3,6,7,8,9,14];
  
  vdata=eegdata;  
  
  % stack spectrograms from all data channels
  P{cnt}=[];
  
  for k=ch
    fprintf('Calculating ch%i...\n',k);
    
    % S is the Fourier transform (amplitude + phase, complex value);
    % F is set of frequencies for S,P (vertical dim);
    % T is set of times for S,P (horizontal dim);
    % P is power spectra (amplitude^2)
    % TT is the length of the window on which to calculate stfft    
    [S,f,T{cnt},p] = spectrogram(vdata(:,k),...
        blackman(tt*128),tt*128-dT*128,8*128,128);
    
    %limit frequencies
    p=p(f>0 & f<=frqthr,:);
    f=f(f>0 & f<=frqthr);   
    
    %sum/average over df bins
    if(df>0)
        pb=[];
        for ff=0:df:frqthr-df
            pb=cat(1,pb,mean(p(f>ff & f<=ff+df,:),1));
        end
        p=pb;
    end    
    
    %stack up
    P{cnt}=cat(1,P{cnt},p);
    
    % convert time to min
    T{cnt}=T{cnt}/60;
    
    %channel size
    dk=size(p,1);
  end
end

save temp P T dk


%% TRAIN
fprintf('##############################\n');
load temp

t_active=9;       % end of active phase, min !set from real data!
t_unfocused=19;   % end of unfocused phase, min !set from real data!
t_sleep_start=21; % start of sleep phase, min !set from data!
t_sleep_end=30;   % end of sleep phase, min !set from data!

%collate data
PP=[];
TT=[];
NID=[];
nids=union(ntrain,ntest);
for cnt=1:length(P)
  PP=cat(2,PP,P{cnt});
  TT=cat(2,TT,T{cnt});
  NID=cat(2,NID,repmat(nids(cnt),size(T{cnt})));
end

%EEG-channel ids
idx=ceil((1:numel(PN))/dk);
NK=reshape(idx,size(PN));


% %noise sample
% PNampl=1;
% PN=randn(size(PP))+i*randn(size(PP));
% PN=abs(PN).^2;
% PN=PNampl*10*log10(PN);
% PN=max(-100,PN);

%limit primary data range
tidx=TT>1 & TT<t_sleep_end;
PP_train=PP(:,tidx);
PN_train=PN(:,tidx);
TT=TT(tidx);
NID=NID(tidx);

%display raw trials
figure(1),imagesc(PP_train),title('Training data set');

%set labels
labels=zeros(size(PP_train,2),1);
labels(TT>0 & TT<t_active)=1;
labels(TT>t_active+2 & TT<t_unfocused)=2;
labels(TT>t_sleep_start & TT<t_sleep_end)=3;

% display mean feature sequence
c={'s','d','o','<','>'};
figure(2),hold on,title('Mean state spectra (dB)'),xlabel('freq'),grid on
for k=unique(NID)
  plot(mean(PP_train(:,labels==1 & NID'==k),2),['k-',c{k}],'LineWidth',2)
  plot(mean(PP_train(:,labels==2 & NID'==k),2),['r-',c{k}],'LineWidth',2)
  plot(mean(PP_train(:,labels==3 & NID'==k),2),['g-',c{k}],'LineWidth',2)
end

%train classifier
nnmax=2000;
sel_train=rand(size(labels))>valthr & ismember(NID',ntrain);
sel=find(sel_train); sel=sel(randperm(length(sel)));
sel=sel(1:min(nnmax,length(sel)));
SVMStruct=cell(1,3);
options=svmsmoset('MaxIter',20000000);
ntuple=max(KK(:));
noise_mod=rand(1,ntuple);
scale_mod=rand(1,ntuple);
%TODO-TODO-TODO
for i=1:3
  fprintf('Training svm%i...\n',i);
  tic
  SVMStruct{i} = svmtrain(PP_train(:,sel)',labels(sel)==i,'Method','LS');      
      %labels_train(train_sel)==i,'Method','SMO','SMO_OPTS',options);
  toc
end

%test
Group=zeros(length(sel),3);
for i=1:3
  Group(:,i)=svmclassify(SVMStruct{i},PP_train(:,sel)');
end
[garbage,GroupT]=max(Group,[],2);
GroupT(sum(Group,2)>1)=0;
GroupS=labels(sel);
trange=GroupS>0;
percentageCorrect = ...
    (sum( GroupS(trange)==GroupT(trange) )/ sum(trange))*100;
fprintf('Validation correct: %g\n',percentageCorrect);

%validation
sel=~sel_train & ismember(NID',ntrain);
Group=zeros(sum(sel),3);
for i=1:3
  Group(:,i)=svmclassify(SVMStruct{i},PP_train(:,sel)');
end
[garbage,GroupT]=max(Group,[],2);
GroupT(sum(Group,2)>1)=0;
GroupS=labels(sel);
trange=GroupS>0;
percentageCorrect = ...
    (sum( GroupS(trange)==GroupT(trange) )/ sum(trange))*100;
fprintf('Validation correct: %g\n',percentageCorrect);

%generalization test
%validation
sel=ismember(NID',ntest);
Group=zeros(sum(sel),3);
for i=1:3
  Group(:,i)=svmclassify(SVMStruct{i},PP_train(:,sel)');
end
[garbage,GroupT]=max(Group,[],2);
GroupT(sum(Group,2)>1)=0;
GroupS=labels(sel);
trange=GroupS>0;
percentageCorrect = ...
    (sum( GroupS(trange)==GroupT(trange) )/ sum(trange))*100;
fprintf('Generalization correct: %g\n',percentageCorrect);

% %% Confusion matrix
% CM=zeros(3,3);
% for i=1:3
%     for j=0:3
%         CM(i,j+1)=sum(labels_test==i & GroupT==j);
%     end
% end
% 
% fprintf('Confision matrix, states vs class 0 1 2 3\n')
% disp(CM)
% 
% fprintf('##############################\n');

% %% Mean-variance analysis
% dk=frqthr/df;
% if(df>0) fp=(df:df:df*dk)'; else fp=f; end
% 
% figure,plot(PP_train')
% hold on
% plot(labels_train*5,'k-','LineWidth',2)
% legf=cell(1,length(fp));
% for i=1:length(fp) legf{i}=sprintf('%i',fp(i)); end
% legend(legf),title('Power time series'),xlabel('Time/samples')
% 
% fprintf('Means-Variance analysis [freq means x3 std x3]\n');
% disp([fp,mean(PP_train(:,labels_train==1),2),...
%     mean(PP_train(:,labels_train==2),2),...
%     mean(PP_train(:,labels_train==3),2),...
%     std(PP_train(:,labels_train==1),[],2),...
%     std(PP_train(:,labels_train==2),[],2),...
%     std(PP_train(:,labels_train==3),[],2)])

%% SVM models
WW=zeros(size(PP_train,1),3);
for i=1:3
    svm2=SVMStruct{i};
    b2=svm2.Bias;
    w2=svm2.SupportVectors'*svm2.Alpha;
    w2=w2.*svm2.ScaleData.scaleFactor';
    b2=b2+svm2.ScaleData.shift*w2;
    w2=-w2;
    WW(:,i)=w2;
end
figure,plot(WW,'-o')
xlabel('freq'),legend('1','2','3'),grid on,title('SVM weights')
