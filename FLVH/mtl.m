X = {};
Y = {};
headerlinesIn = 0;
for fold = 1:3
    for i = 0:9

    %     D =  csvread('/home/miley/Documents/AAAI2018/flavor2_'+string(i)+'.csv',1,2);
        D = importdata('tau=1_k=10\train\fold_'+string(fold)+'\task_'+string(i)+'.csv');
        D = D.data;
    %     D = D(:,2:18);
        X{1,i+1} = D(:,2:19);
        Y{1,i+1} = D(:,20);
    end

    lambda = [1000];

    %rng('default');     % reset random generator. Available from Matlab 2011.
    opts.init = 0;      % guess start point from data. 
    opts.tFlag = 1;     % terminate after relative objective value does not changes much.
    opts.tol = 10^-5;   % tolerance. 
    opts.maxIter = 1500; % maximum iteration number of optimization.

    sparsity = zeros(length(lambda), 1);
    log_lam  = log(lambda);
    [W,funcVal] = Least_TGL(X, Y,1000,1000,lambda);
%     if (exist('C:\Users\miley\Documents\MTL new\harris formulation\tau=1_k=10/W/fold_'+string(fold))==0)
%             mkdir('C:\Users\miley\Documents\MTL new\harris formulation\tau=1_k=10/W/fold_'+string(fold))
%     end
    save('tau=1_k=10/W/fold_'+string(fold)+'/W_'+string(lambda)+'_new.mat','W')
end