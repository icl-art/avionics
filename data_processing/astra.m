clear
close all
clc

%TEST

G = 9.8065;

col1 = '#2978a0';
col2 = '#BA1200';
col3 = '#3EC300';
col4 = '#3C153B';
lw = 1;
launch = 'astra_jun13';

% load OpenRocket.mat

data = readmatrix(sprintf('%s.csv', launch));
data = sortrows(data);

t = data(:, 1);
pressure = data(:, 2);
temp = data(:, 3);
acc_x = data(:, 4)*G;
acc_y = data(:, 5)*G;
acc_z = data(:, 6)*G;
acc_magnitude = sqrt(acc_x.^2 + acc_y.^2 + acc_z.^2);
g_x = data(:, 7);
g_y = data(:, 8);
g_z = data(:, 9);

% convert from ms to s
t = t/1000;
% shift t values to recording start
t = t - min(t);

period = 5;

% new_x = movmean(-acc_z,period);
% new_y = movmean(acc_y,period);
% new_z = movmean(acc_x,period);

new_x = movmean(acc_x, period);
new_y = movmean(acc_y, period);
new_z = movmean(acc_z, period);

figure
hold on
plot(t, new_x, 'LineWidth', lw, 'Color', col1)
plot(t, new_y, 'LineWidth', lw, 'Color', col2)
plot(t, new_z, 'LineWidth', lw, 'Color', col3)
plot(t, acc_magnitude, 'LineWidth', 1, 'Color', col4)
% plot(time2, OR_accel, 'c-', 'LineWidth', lw)
title('Acceleration - Custom');
xlabel('Time (s)')
ylabel('Acceleration (m/s^2)')
legend('x', 'y', 'z', 'Magnitude', 'OpenRocket', 'Location', 'best')
xlim([275 325])
% ylim([-80 109])
exportgraphics(gcf, sprintf('%s_acceleration.png', launch), 'Resolution', 600);

period = 10;

g_x = movmean(g_x,period);
g_y = movmean(g_y,period);
g_z = movmean(g_z,period);

figure
hold on
plot(t, g_x, 'LineWidth', lw, 'Color', col1)
plot(t, g_y, 'LineWidth', lw, 'Color', col2)
plot(t, g_z, 'LineWidth', lw, 'Color', col3)
% plot(time2, OR_angVel, 'c-', 'LineWidth', lw)
title('Angular Velocity - Custom');
xlabel('Time (s)')
ylabel('Rotation (deg/s)')
legend('x', 'y', 'z', 'OpenRocket', 'Location', 'best')
% xlim([275 325])
% exportgraphics(gcf, sprintf('%s_rotation.png', launch), 'Resolution', 600);

figure
plot(t, pressure, 'LineWidth', lw, 'Color', col1)
title('Pressure - Custom')
xlabel('Time(s)')
ylabel('Pressure (Pa)')
xlim([275 325])
exportgraphics(gcf, sprintf('%s_pressure.png', launch), 'Resolution', 600);

% inp = input('Run ASTRA MkII Cleaner?');
inp = true;

if inp == true
    
    height = atmospalt(pressure);
    
    skips = [];
    
    for i = 2:length(height);
        if height(i) == height(i-1)
            
            skips(end+1) = i;
            
        end
        
    end
    
    height(skips) = 0;
    
    t_filtered = t(height~=0);
    height  = height(height~=0);
    height = height - min(height);
    
    custom_vel = zeros(length(height),1);
    
    for i = 1:length(height)-1
        
        custom_vel(i) = (height(i+1)-height(i))/(t_filtered(i+1)-t_filtered(i));
        
    end
    
    figure
    hold on
    plot(t_filtered, height, 'LineWidth', lw, 'Color', col2)
    yline(max(height),'--')
    hold off
    title('Altitude ASL - Custom')
    xlabel('Time(s)')
    ylabel('Altitude (m)')
    xlim([275 325])
    exportgraphics(gcf, sprintf('%s_altitude.png', launch), 'Resolution', 600);
    
    figure
    plot(t_filtered, custom_vel, 'LineWidth', lw, 'Color', col2)
    title('Velocity - Custom')
    xlabel('Time(s)')
    ylabel('Velocity (ms^{-1})')
    xlim([275 325])
    exportgraphics(gcf, sprintf('%s_velocity.png', launch), 'Resolution', 600);
    
    
else
    
    height = atmospalt(pressure);
    
    figure
    plot(t, height, 'LineWidth', lw, 'Color', col2)
    title('Altitude ASL - Custom')
    xlabel('Time(s)')
    ylabel('Altitude (m)')
    xlim([275 325])
    exportgraphics(gcf, sprintf('%s_altitude.png', launch), 'Resolution', 600);
    
    
end

figure
plot(t, temp, 'LineWidth', lw, 'Color', col3)
title('Temperature - Custom');
xlabel('Time(s)');
ylabel('Temperature (C)');
xlim([275 325])
exportgraphics(gcf, sprintf('%s_temperature.png', launch), 'Resolution', 600);

figure
plot(t, 'LineWidth', lw, 'Color', col4)
title('Data Recording - Custom')
box on
xlabel('Data Point');
ylabel('Time Elapsed')
exportgraphics(gcf, sprintf('%s_recording.png', launch), 'Resolution', 600);

pnut = importdata(sprintf('%s.pf2', launch), ',', 11).data;

t = pnut(:, 1);
altitude = pnut(:, 2)./3.281;
vel = pnut(:, 3)./3.281;
temp = pnut(:, 4);

altitude(t==12.35) = 531;

figure
hold on
plot(t, altitude, 'LineWidth', lw, 'Color', col1)
yline(max(altitude), '--')
% plot(time+0.4,OR_alt, '-.', 'LineWidth', lw, 'Color', col2)
hold off
title('Altitude AGL - Pnut')
legend('Pnut', 'OpenRocket', 'Location', 'best')
xlabel('Time(s)')
box on
ylabel('Altitude (m)')
exportgraphics(gcf, sprintf('%s_altitude_pnut.png', launch), 'Resolution', 600);

period = 35;

smooth_alt = movmean(altitude,period);
disp(['Moving average period = ' num2str(period) ', and apogee = ' num2str(max(smooth_alt)) ' m'])

figure
hold on
plot(t, smooth_alt, 'LineWidth', lw, 'Color', col1)
% plot(time+0.4,OR_alt, '-.', 'LineWidth', lw, 'Color', col2)
hold off
title('Smoothed Altitude AGL - Pnut')
legend('Pnut', 'OpenRocket', 'Location', 'best')
xlabel('Time(s)')
ylabel('Altitude (m)')
box on
exportgraphics(gcf, sprintf('%s_smoothed_altitude_pnut.png', launch), 'Resolution', 600);

figure
plot(t, vel, 'LineWidth', lw, 'Color', col2)
hold on
% plot(time, OR_vel, 'LineWidth', lw, 'Color', col3)
hold off
title('Velocity - Pnut')
legend('Pnut', 'OpenRocket', 'Location', 'best')
xlabel('Time(s)')
box on
ylabel('Velocity (m/s)')
exportgraphics(gcf, sprintf('%s_velocity_pnut.png', launch), 'Resolution', 600);

figure
plot(t, temp, 'LineWidth', lw, 'Color', col3)
title('Temperature - Pnut')
xlabel('Time(s)')
ylabel('Temperature (C)')
box on
exportgraphics(gcf, sprintf('%s_temperature_pnut.png', launch), 'Resolution', 600);

OR = readmatrix('OR_astra_jun13.csv');
OR_t = OR(:,1);
OR_alt = OR(:,2);
OR_vel = OR(:,3);
OR_acc = OR(:,4);

% inp = input('Run ASTRA MkII PNut comparison?');

inp = true;

if inp == true
    
    figure
    hold on
    plot(t, altitude, 'LineWidth', lw, 'Color', col1)
    plot(t_filtered-280.3, height-6.2, 'LineWidth', lw, 'Color', col2)
    % plot(time+0.4,OR_alt, '-.', 'LineWidth', lw, 'Color', col2)
    hold off
    title('Altitude AGL')
    legend('Pnut', 'Custom Bay', 'Location', 'best')
    xlim([0 50])
    box on
    xlabel('Time(s)')
    ylabel('Altitude (m)')
    exportgraphics(gcf, sprintf('%s_altitude_combined.png', launch), 'Resolution', 600);
    
    figure
    hold on
    plot(t, vel, 'LineWidth', lw, 'Color', col1)
    plot(t_filtered-280.3+0.512, custom_vel, 'LineWidth', lw, 'Color', col2)
    % plot(time+0.4,OR_alt, '-.', 'LineWidth', lw, 'Color', col2)
    hold off
    title('Velocity')
    box on
    legend('Pnut', 'Custom Bay', 'Location', 'best')
    xlim([0 50])
    xlabel('Time(s)')
    ylabel('Velocity (ms^{-1})')
    exportgraphics(gcf, sprintf('%s_velocity_combined.png', launch), 'Resolution', 600);
    
    figure
    tiledlayout(2,1)
    nexttile
    hold on
    plot(t, altitude, '-.', 'LineWidth', lw, 'Color', col1)
    plot(t_filtered-280.3, height-6.2, 'LineWidth', lw*0.8, 'Color', col2)
    % plot(time+0.4,OR_alt, '-.', 'LineWidth', lw, 'Color', col2)
    hold off
    title('Altitude AGL')
    legend('Commercial Avionics (Pnut)', 'Custom Avionics', 'Location', 'best')
    xlim([0 50])
    box on
    xlabel('Time(s)')
    ylabel('Altitude (m)')
    
    nexttile
    hold on
    plot(t, vel, '-.', 'LineWidth', lw, 'Color', col1)
    plot(t_filtered-280.3+0.512, custom_vel,'LineWidth', lw*0.8, 'Color', col2)
    % plot(time+0.4,OR_alt, '-.', 'LineWidth', lw, 'Color', col2)
    hold off
    title('Velocity')
    box on
    legend('Commercial Avionics (Pnut)', 'Custom Avionics', 'Location', 'best')
    xlim([0 50])
    xlabel('Time(s)')
    ylabel('Velocity (ms^{-1})')    
    exportgraphics(gcf, sprintf('%s_all_combined.png', launch), 'Resolution', 600);
    
end

% close all
