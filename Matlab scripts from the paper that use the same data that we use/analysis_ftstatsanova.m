% TOP FEATURES BY ANOVA/ICC

subject='MKL';               %subject identifier
include=[0,1,1,1,1,1,0];    %damaged or bad experiments (mk)
% include=[1,1,1,1,1,0,0];    %damaged or bad experiments (us)
% include=[0,1,1,1,1,1,0];    %damaged or bad experiments (es)
% include=[1,1,1,1,0,1,0];    %damaged or bad experiments (ge)
% include=[1,1,1,1,1,0,0];    %damaged or bad experiments (ds)
outfname='out_mk.xlsx';

%% EXTRACT FEATURES
analysis_prepft

%% GROUP VARIABLES
nft=size(PP_train,1);
groups=cell(1,3);
for c=1:3
    groups{c}=PP_train(:,labels==c);
end

%% GROUP MEAN AND VARIANCES
mm=mean(PP_train,2);
ms=zeros(nft,3);
ss=zeros(nft,3);
ns=zeros(1,3);
for c=1:3
    ms(:,c)=mean(groups{c},2);
    ss(:,c)=var(groups{c},1,2);
    ns(1,c)=size(groups{c},2);
end

%% F-STATISTICS
K=3;
N=size(PP_train,2);
ns_r=repmat(ns,nft,1);
ms_diff=bsxfun(@minus,ms,mm);
var_expl=sum(ns_r.*ms_diff.^2,2)/(K-1);
var_res=sum(ns_r.*ss,2)/(N-K);
F=var_expl./var_res;

%% ICC
var_mean=var(ms,1,2);
var_tot=var(PP_train,1,2);
ICC=var_mean./var_tot;

%% LIST
M=length(ICC);
[a,b]=sort(ICC,'descend');
idx=b(1:M)';
[frq,ch]=ind2sub([36,7],idx(:));

 X=[ch,frq/2,mm(idx),sqrt(var_tot(idx)),ms(idx,:),ICC(idx),F(idx)/1000];
 xlswrite(outfname,X);
 disp(X)
 
  