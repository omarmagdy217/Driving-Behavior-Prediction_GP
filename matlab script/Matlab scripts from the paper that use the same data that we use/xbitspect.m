%OPERATOR STATE ANALYZER
% clear,clc,close all

valthr=0.25;            %fraction of validation samples


%% OPTIONS
frqthr=15;              %high frequency threshold {try 35,30,25,20,15,10}
TT=30;                  %spectrogram window, sec {try 1,2,3,5,10,15,30,45,60}
dT=1;                   %spectrogram T-step, sec
df=1;                   %average power into [df Hz]-bands {try somethng}
dftype=1;               %type of band-power averages {try 1,2}
normalize=false;        %normalize raws {try true/false}
sumch=true;             %average powers over all channels {try true/false}
TA=ceil(30/dT);         %average power over time {try values 0-60}

ntrain=[1,3,4];         %try different splits of train/test datasets
ntest=[5];


%% LOAD DATA
load eegkaydi1.mat
O{1}=o;

load eegkaydi2.mat
O{2}=o;

load eegkaydi3.mat
O{3}=o;

load eegkaydi4.mat
O{4}=o;

load eegkaydi5.mat
O{5}=o;

%(!) load eegkaydi.mat FIRST (!)
% EEG data is o.data(:,4:17)

nn=length(O);
P_full=cell(1,nn);
T=cell(1,nn);
for cnt=union(ntrain,ntest)
  eegdata=O{cnt}.data(:,4:17);
  
  % valid channels
  ch=[2,3,6,7,8,9,14];
  
  vdata=eegdata;  
  
  % stack spectrograms from all data channels
  P_full{cnt}=[];
  
  for k=ch
    fprintf('Calculating ch%i...\n',k);
    
    % S is the Fourier transform (amplitude + phase, complex value);
    % F is set of frequencies for S,P (vertical dim);
    % T is set of times for S,P (horizontal dim);
    % P is power spectra (amplitude^2)
    % TT is the length of the window on which to calculate stfft    
    [S,f,T{cnt},p] = spectrogram(vdata(:,k),...
        blackman(TT*128),TT*128-dT*128,8*128,128);
    
    %limit frequencies
    p=p(f>0 & f<=frqthr,:);
    f=f(f>0 & f<=frqthr);   
    
    %mean power per df frequency-band (true power)
    if(df>0 && dftype==1)
        pb=[];
        for ff=0:df:frqthr-df
            pb=cat(1,pb,mean(p(f>ff & f<=ff+df,:).^2,1));
        end
        p=pb;
    end

    p=10*log10(p);
    p=max(-100,p);    
    
    %Uncomment to normalize each time's sample
    if(normalize)
        %normalize
        p_mean=mean(p,1);
        p_std=std(p,[],1);
        p=(p-repmat(p_mean,size(p,1),1))./repmat(p_std,size(p,1),1);
    end
    
    %mean dB power per df frequency band
    if(df>0 && dftype==2)
        pb=[];
        for ff=0:df:frqthr-df
            pb=cat(1,pb,mean(p(f>ff & f<=ff+df,:),1));
        end
        p=pb;
    end

    dk=size(p,1);
        
    %stack spectrograms
    P_full{cnt}=cat(1,P_full{cnt},p);
    
    % convert time to mins
    T{cnt}=T{cnt}/60;
  end
end

save temp P_full T
load temp

fprintf('##############################\n');

%% TRAIN
% load temp

t_active=9;      % end of active phase, min !set from real data!
t_unfocused=19;   % end of unfocused phase, min !set from real data!
t_sleep_start=21; % start of sleep alpha waves, min !set from data!
t_sleep_end=30;   % end of sleep alpha waves, min !set from data!

%collate data
PP=[];
TT=[];
for cnt=ntrain
  PP=cat(2,PP,P_full{cnt});
  TT=cat(2,TT,T{cnt});
end

%average power from all channels
if(sumch)
    pb=[];
    for k=1:dk
        pb=cat(1,pb,mean(PP(k:dk:end,:),1));
    end
    PP=pb;
end

%average over time 
if(TA>0)
   PP=filter(1/TA*ones(1,TA),1,PP,[],2); 
end

%limit data range
tidx=TT>1 & TT<t_sleep_end;
PP_train=PP(:,tidx);
TT=TT(tidx);

%svmtrain
labels_train=zeros(size(PP_train,2),1);
labels_train(TT>0 & TT<t_active)=1;
labels_train(TT>t_active+2 & TT<t_unfocused)=2;
labels_train(TT>t_sleep_start & TT<t_sleep_end)=3;
train_sel=rand(size(labels_train))>valthr;
SVMStruct=cell(1,3);
options=svmsmoset('MaxIter',20000000);
for i=1:3
  fprintf('Training svm%i...\n',i);
  tic
  SVMStruct{i} = svmtrain(PP_train(:,train_sel)',...
      labels_train(train_sel)==i,'Method','LS');      
      %labels_train(train_sel)==i,'Method','SMO','SMO_OPTS',options);
  toc
end
% save svmmodel SVMStruct
% load svmmodel

%test-1
Group=zeros(sum(train_sel),3);
for i=1:3
  Group(:,i)=svmclassify(SVMStruct{i},PP_train(:,train_sel)');
end
[garbage,GroupT]=max(Group,[],2);
GroupT(sum(Group,2)>1)=0;


labels=labels_train(train_sel);
trange=labels>0;
percentageCorrect = ...
    (sum( labels(trange)==GroupT(trange) )/ sum(trange))*100;
fprintf('Percentage correct (train): %g\n',percentageCorrect);

%test-2
Group=zeros(sum(~train_sel),3);
for i=1:3
  Group(:,i)=svmclassify(SVMStruct{i},PP_train(:,~train_sel)');
end
[garbage,GroupT]=max(Group,[],2);
GroupT(sum(Group,2)>1)=0;

labels=labels_train(~train_sel);
trange=labels>0;
percentageCorrect = ...
    (sum( labels(trange)==GroupT(trange) )/ sum(trange))*100;
fprintf('Percentage correct (validation): %g\n',percentageCorrect);

%% TEST
%collate data
PP=[];
TT=[];
for cnt=ntest
  PP=cat(2,PP,P_full{cnt});
  TT=cat(2,TT,T{cnt});
end

%average power on all channels
if(sumch)    
    pb=[];
    for k=1:dk
        pb=cat(1,pb,mean(PP(k:dk:end,:),1));
    end
    PP=pb;
end

%average over time 
if(TA>0)
   PP=filter(1/TA*ones(1,TA),1,PP,[],2); 
end

%limit data
tidx=TT>1 & TT<t_sleep_end;
PP_test=PP(:,tidx);
TT=TT(tidx);

%test-3
labels_test=zeros(size(PP_test,2),1);
labels_test(TT>0 & TT<t_active)=1;
labels_test(TT>t_active+2 & TT<t_unfocused)=2;
labels_test(TT>t_sleep_start & TT<t_sleep_end)=3;
Group=zeros(size(labels_test,1),3);
for i=1:3
  Group(:,i)=svmclassify(SVMStruct{i},PP_test');
end
[garbage,GroupT]=max(Group,[],2);
GroupT(sum(Group,2)>1)=0;

labels=labels_test;
trange=labels>0;
percentageCorrect = ...
    (sum( labels(trange)==GroupT(trange) )/ sum(trange))*100;
fprintf('Percentage correct (test): %g\n',percentageCorrect);

%% Train dataset visual
figure,imagesc(PP_train),title('Training data set');

%% Confusion matrix
CM=zeros(3,3);
for i=1:3
    for j=0:3
        CM(i,j+1)=sum(labels_test==i & GroupT==j);
    end
end

fprintf('Confision matrix, states vs class 0 1 2 3\n')
disp(CM)

return

fprintf('##############################\n');

%% Mean-variance analysis
if(df>0) fp=(df:df:df*dk)'; else fp=f; end

figure,plot(PP_train')
hold on
plot(labels_train*5,'k-','LineWidth',2)
legf=cell(1,length(fp));
for i=1:length(fp) legf{i}=sprintf('%i',fp(i)); end
legend(legf),title('Power time series'),xlabel('Time/samples')

fprintf('Means-Variance analysis [freq means x3 std x3]\n');
disp([fp,mean(PP_train(:,labels_train==1),2),...
    mean(PP_train(:,labels_train==2),2),...
    mean(PP_train(:,labels_train==3),2),...
    std(PP_train(:,labels_train==1),[],2),...
    std(PP_train(:,labels_train==2),[],2),...
    std(PP_train(:,labels_train==3),[],2)])

%% Graphs
figure
plot(mean(PP_train(:,labels_train==1),2),'b-')
hold on
plot(mean(PP_train(:,labels_train==2),2),'g-')
plot(mean(PP_train(:,labels_train==3),2),'r-')
plot(mean(PP_test(:,labels_test==1),2),'b--')
plot(mean(PP_test(:,labels_test==2),2),'g--')
plot(mean(PP_test(:,labels_test==3),2),'r--')
xlabel('freq'),legend('1','2','3')
title('Mean state spectra')



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

if(df>0) fp=(df:df:df*dk)'; else fp=f; end
fprintf('States SVM-weights, freq W x3\n');
disp([fp,WW])