clear

v = VideoReader('TreesIn.mp4');
frame = read(v, 1);
imshow(frame)
title('Original Frame')

% frame = im2double(frame);
frame = imread('Logo3.png');
% load pretrained models
deblocknet = load('pretrainedJPEGDnCNN.mat').net;
upscalenet = load('trainedVDSR-Epoch-100-ScaleFactors-234.mat').net;

% target resolution - 4:3 aspect ratio, 2x orig
target_h = 960*2;
target_w = 1280*2;
target_channels = 3; % rgb image

% performance tracking
tic

% convert RGB image to luminance and chrominance 
Iycbcr = rgb2ycbcr(frame);
Iy = Iycbcr(:, :, 1);
Icb = Iycbcr(:, :, 2);
Icr = Iycbcr(:, :, 3);

Iy_bicubic = imresize(Iy, [target_h target_w], 'bicubic');
Icb_bicubic = imresize(Icb, [target_h target_w], 'bicubic');
Icr_bicubic = imresize(Icr, [target_h target_w], 'bicubic');

disp('AI Magic Time');

% deblocking does not yield a visible benefit in this case
% Iy = denoiseImage(Iy, deblocknet);
Iresidual = activations(upscalenet, Iy_bicubic, 41);
% Iresidual = activations(upscalenet, Iy, 41);
disp('Voodoo Complete');

Iresidual = double(Iresidual);

Isr = Iy_bicubic + Iresidual;
% Isr = Iy + Iresidual;

upscaled_ycbcr = cat(3, Isr, Icb_bicubic, Icr_bicubic);
% upscaled_ycbcr = cat(3, Isr, Icb, Icr);
upscaled = ycbcr2rgb(upscaled_ycbcr);

toc

% imshow(upscaled)
% title('upscaled');
imwrite(upscaled, 'logo_upscaled.png')

% denoising does not yield a visible benefit in this case
% tic
% denoisenet = denoisingNetwork('dncnn');
% [noisyR, noisyG, noisyB] = imsplit(upscaled);
% disp('Denoising')
% denoisedR = denoiseImage(noisyR, denoisenet);
% denoisedG = denoiseImage(noisyG, denoisenet);
% denoisedB = denoiseImage(noisyB, denoisenet);
% denoised = cat(3, denoisedR, denoisedG, denoisedB);
% disp('Done')
% toc
% 
% imshow(denoised);
% title('upscaled, denoised');
% imwrite(denoised, 'frame1_upscaled_denoised.png')
% montage({frame, upscaled, denoised})

clear