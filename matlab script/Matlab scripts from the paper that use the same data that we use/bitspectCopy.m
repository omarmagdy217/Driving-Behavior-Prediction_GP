%IMPORT EEG DATA FOR SVM, BASED ON SLOW SPECTROGRAM
%clear all

 frqthr=20;
%  expids=1:5;
 %expids=1;

% DEBUGED !!
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
P_full=cell(1,5);
T=cell(1,5);
for cnt=1:5       % expids  % cnt=1:5
    eegdata=O{cnt}.data(:,4:17);
    
    % valid channels by labels 2,3,5,6,7,8,9,10,14==F7,F3,T7,P7,O1,O2,P8,T8,AF4
    % references: T7/T8=5,10
    % (!) may need adjustment for some experiments, see actual spectrograms
    
    %%ch=[2,3,5,6,7,8,9,10,14];
    ch=[2,3,6,7,8,9,14];
    
    vdata=eegdata;
    
    
    %% stack spectrograms from all data channels
    P_full{cnt}=[];

    
    for k=ch
        fprintf('Calculating ch%i...\n',k);
        
        %Here
        % S is the Fourier transform (amplitude + phase, complex value);
        % F is set of frequencies for S,P (vertical dim);
        % T is set of times for S,P (horizontal dim);
        % P is power spectra (amplitude^2)
        % TT is the length of the window on which to calculate stfft
        TT=15;
        
        [S,f,T{cnt},p] = spectrogram(vdata(:,k),blackman(TT*128),TT*128-64,8*128,128);
        
        %remove zero-frequency==constant bias
        p=p(f>0 & f<20,:);
        f=f(f>0 & f<20);
        
        %this is the same as P_full=[P_full;P] but avoids "growing" warning
        P_full{cnt}=cat(1,P_full{cnt},p);
   
        % convert time to mins
        T{cnt}=T{cnt}/60;
    end
end
% save temp.mat P_full T








% DEBUGED
% load spectras
PP_full=[];
TT_full=[];
for cnt=1:5

    PP_full=cat(2,PP_full,P_full{cnt});
    TT_full=cat(2,TT_full,T{cnt});
    
end
PP_full=10*log10(PP_full);
PP_full=max(-100,PP_full);

%clear P_full T
% load spectramerged


t_active=10;      % end of active phase, min !set from real data!
t_unfocused=20;   % end of unfocused phase, min !set from real data!
t_sleep_start=20; % start of sleep alpha waves, min !set from data!
t_sleep_end=35;   % end of sleep alpha waves, min !set from data!

Cell_full_active=PP_full(:,TT_full>0 & TT_full<t_active);
Cell_full_unfocused=PP_full(:,TT_full>t_active & TT_full<t_unfocused);
Cell_full_sleep=PP_full(:,TT_full>t_sleep_start & TT_full<t_sleep_end);







% TRAIN!!!!
%
T_A=transpose(Cell_full_active(:,rand(1,size(Cell_full_active,2))<0.20));
T_U=transpose(Cell_full_unfocused(:,rand(1,size(Cell_full_unfocused,2))<0.20));
T_S=transpose(Cell_full_sleep(:,rand(1,size(Cell_full_sleep,2))<0.20));

training = [T_A;T_U;T_S];




%training=training2;

%train
L_A=size(T_A,1);
L_U=size(T_U,1);
L_S=size(T_S,1);

class=zeros(size(training,1),1);
class(1:L_A)=1;
class(L_A+1:L_A+L_U)=2;
class(L_A+L_U+1:L_A+L_U+L_S)=3;

options=svmsmoset('MaxIter',20000000);
SVMStruct1 = svmtrain(training,class==1,'Method','SMO','SMO_OPTS',options);
SVMStruct2 = svmtrain(training,class==2,'Method','SMO','SMO_OPTS',options);
SVMStruct3 = svmtrain(training,class==3,'Method','SMO','SMO_OPTS',options);

save SVMStruct1 SVMStruct1
save SVMStruct2 SVMStruct2
save SVMStruct3 SVMStruct3

%% TEST!!!

for sayac=1:5
 PPU_full=[];
TTU_full=[];

    PPU_full=cat(2,PPU_full,P_full{sayac});
    TTU_full=cat(2,TTU_full,T{sayac});
    

PPU_full=10*log10(PPU_full);
PPU_full=max(-100,PPU_full);


Cell_full_active1=PPU_full(:,TTU_full>0 & TTU_full<t_active);
Cell_full_unfocused1=PPU_full(:,TTU_full>t_active & TTU_full<t_unfocused);
Cell_full_sleep1=PPU_full(:,TTU_full>t_sleep_start & TTU_full<t_sleep_end);




T_A1=transpose(Cell_full_active1(:,rand(1,size(Cell_full_active1,2))<0.50));
T_U1=transpose(Cell_full_unfocused1(:,rand(1,size(Cell_full_unfocused1,2))<0.50));
T_S1=transpose(Cell_full_sleep1(:,rand(1,size(Cell_full_sleep1,2))<0.50));

 testset = [T_A1;T_U1;T_S1];
 

 
 %testset = k;
 
L_A1=size(T_A1,1);
L_U1=size(T_U1,1);
L_S1=size(T_S1,1);

%classtest=zeros(size(testset,1),1);
%classtest(1:L_A1)=1;
%classtest(L_A1+1:L_A1+L_U1)=2;
%classtest(L_A1+L_U1+1:L_A1+L_U1+L_S1)=3;

classtest=zeros(size(testset,1),1);
classtest(1:L_A1)=1;
classtest(L_A1+1:L_A1+L_U1)=2;
classtest(L_A1+L_U1+1:L_A1+L_U1+L_S1)=3;


Group1=svmclassify(SVMStruct1,testset);
Group2=svmclassify(SVMStruct2,testset);
Group3=svmclassify(SVMStruct3,testset);


GroupT=zeros(size(Group1));
for i=1:size(Group1,1)
 if Group1(i)==1 & Group2(i)==0 & Group3(i)==0
     GroupT(i)=1;       
  else
        if Group1(i)==0 & Group2(i)==1 & Group3(i)==0
            GroupT(i)=2;
        else
            if Group1(i)==0 & Group2(i)==0 & Group3(i)==1
            GroupT(i)=3;
            else
                GroupT(i)=0;
            end
        end

  end
end

percentageCorrect = (sum( classtest==GroupT )/length(GroupT))*100;
fprintf('Percentage correct: %g\n',percentageCorrect);

end