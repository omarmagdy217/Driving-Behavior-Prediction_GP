% MENTAL STATE DETECTION FROM EEG
close all

%% OPTIONS
subject='MK';               %subject identifier
include=[0,1,1,1,1,1,0];    %damaged or bad experiments (mk)
% include=[1,1,1,1,1,0,0];    %damaged or bad experiments (us)
% include=[0,1,1,1,1,1,0];    %damaged or bad experiments (es)
% include=[1,1,1,1,0,1,0];    %damaged or bad experiments (ge)
% include=[1,1,1,1,1,0,0];    %damaged or bad experiments (ds)


%% EXTRACT FEATURES
analysis_prepft

%% TRAIN THE DETECTOR
SVMStruct=cell(1,3);
for i=1:3
    SVMStruct{i} = svmtrain(PP_train(:,train_sel)',...
        labels(train_sel)==i,'Method','LS');
end

%validation
Group=zeros(sum(~train_sel),3);
for i=1:3
    Group(:,i)=svmclassify(SVMStruct{i},PP_train(:,~train_sel)');
end
[garbage,GroupT]=max(Group,[],2);

%zero out detection when more than 1 classifier responded
GroupT(sum(Group,2)>1)=0;

%produce performance evaluation for each experiment separately
labels_chk=labels(~train_sel);
for cnt=1:nn
    trange=labels_chk>0 & ID(~train_sel)'==cnt;
    percCorrect=mean(labels_chk(trange)==GroupT(trange))*100;
    fprintf('Validation correct, experiment #%i: %g\n',cnt,percCorrect);
end

%produce performance evaluation on all experiments
trange=labels_chk>0;
percCorrect=mean(labels_chk(trange)==GroupT(trange))*100;
fprintf('Validation correct, average: %g\n',percCorrect);








