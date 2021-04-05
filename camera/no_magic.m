clear
close all

v = VideoReader('TreesIn.mp4');
frame = read(v, 1);
% frame = double(frame);
% imshow(frame)
% title('Original Frame')



frame_lab = rgb2lab(frame);

% normalise luminosity 
luminosity = frame_lab(:, :, 1)/100;

boost_contrast_lab = frame_lab;
boost_contrast_lab(:, :, 1) = adapthisteq(luminosity)*100;
boost_contrast = lab2rgb(boost_contrast_lab);

[dehazed, haze, light] = imreducehaze(frame, 'Method', 'approxdcp', 'ContrastEnhancement', 'none');

sharpened = imsharpen(boost_contrast);

montage({frame, dehazed, boost_contrast, sharpened})
title('Orig / Dehazed / Contrast Boosted / Sharpened')