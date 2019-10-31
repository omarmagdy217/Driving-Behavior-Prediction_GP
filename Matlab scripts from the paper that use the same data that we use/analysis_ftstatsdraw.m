%draw feature statistics
close all

subject='MK';               %subject identifier
include=[0,1,1,1,1,1,0];    %damaged or bad experiments (mk)
% include=[1,1,1,1,1,0,0];    %damaged or bad experiments (us)
% include=[0,1,1,1,1,1,0];    %damaged or bad experiments (es)
% include=[1,1,1,1,0,1,0];    %damaged or bad experiments (ge)
% include=[1,1,1,1,1,0,0];    %damaged or bad experiments (ds)

%% EXTRACT FEATURES
analysis_prepft

%% FEATURE MEAN AND VARIANCES
ms=mean(PP_train,2);
ss=std(PP_train,0,2);

%% DRAW MEANS AND STD
close all
for c=1:7
    range=36*(c-1)+1:36*c;
    figure
    bar(0.5:0.5:18,ms(range))
    hold on
    plot(0.5:0.5:18,ss(range),'r--')
    figname=sprintf('ftstats%i.fig',c);
    savefig(figname)
end

%% GROUP MEAN AND VARIANCES
close all
nft=size(PP_train,1);
ms=zeros(nft,3);
ss=zeros(nft,3);
ns=zeros(1,3);
for c=1:3
    ms(:,c)=mean(PP_train(:,labels==c),2);
    ss(:,c)=var(PP_train(:,labels==c),1,2);
    ns(1,c)=size(PP_train(:,labels==c),2);
end

for c=1:7
    figure
    hold all
    for g=1:3
        range=36*(c-1)+1:36*c;
        errorbar(0.5:0.5:18,ms(range,g),ss(range,g))
    end
    box on, grid on
    figname=sprintf('dftstats%i.fig',c);
    savefig(figname)    
end