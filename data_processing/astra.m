clear

G = 9.8065;

col1 = '#2978a0';
col2 = '#BA1200';
col3 = '#3EC300';
col4 = '#3C153B';
lw = 1;
launch = 'astra_apr11';

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

figure
hold on
plot(t, acc_x, 'LineWidth', lw, 'Color', col1)
plot(t, acc_y, 'LineWidth', lw, 'Color', col2)
plot(t, acc_z, 'LineWidth', lw, 'Color', col3)
plot(t, acc_magnitude, 'LineWidth', 1, 'Color', col4)
title('Acceleration - 💩📦');
xlabel('Time (s)')
ylabel('Acceleration (m/s^2)')
legend('x', 'y', 'z', 'Magnitude', 'Location', 'best')
xlim([(min(t)-1), (max(t)+1)])
exportgraphics(gcf, sprintf('%s_acceleration.png', launch), 'Resolution', 600);

figure
hold on
plot(t, g_x, 'LineWidth', lw, 'Color', col1)
plot(t, g_y, 'LineWidth', lw, 'Color', col2)
plot(t, g_z, 'LineWidth', lw, 'Color', col3)
title('Angular Velocity - 💩📦');
xlabel('Time (s)')
ylabel('Rotation (deg/s)')
legend('x', 'y', 'z', 'Location', 'best')
xlim([(min(t)-1), (max(t)+1)])
exportgraphics(gcf, sprintf('%s_rotation.png', launch), 'Resolution', 600);

figure
plot(t, pressure, 'LineWidth', lw, 'Color', col1)
title('Pressure')
xlabel('Time(s)')
ylabel('Pressure (Pa) - 💩📦')
xlim([(min(t)-1), (max(t)+1)])
exportgraphics(gcf, sprintf('%s_pressure.png', launch), 'Resolution', 600);

height = atmospalt(pressure);
figure
plot(t, height, 'LineWidth', lw, 'Color', col2)
title('Altitude ASL - 💩📦')
xlabel('Time(s)')
ylabel('Altitude (m)')
xlim([(min(t)-1), (max(t)+1)])
exportgraphics(gcf, sprintf('%s_altitude.png', launch), 'Resolution', 600);

figure
plot(t, temp, 'LineWidth', lw, 'Color', col3)
title('Temperature - 💩📦');
xlabel('Time(s)');
ylabel('Temperature (C)');
xlim([(min(t)-1), (max(t)+1)])
exportgraphics(gcf, sprintf('%s_temperature.png', launch), 'Resolution', 600);

figure
plot(t, 'LineWidth', lw, 'Color', col4)
title('Data Recording - 💩📦')
xlabel('Data Point');
ylabel('Time Elapsed')
exportgraphics(gcf, sprintf('%s_recording.png', launch), 'Resolution', 600);

pnut = importdata(sprintf('%s.pf2', launch), ',', 11).data;

t = pnut(:, 1);
altitude = pnut(:, 2)./3.281;
vel = pnut(:, 3)./3.281;
temp = pnut(:, 4);

figure
plot(t, altitude, 'LineWidth', lw, 'Color', col1)
title('Altitude AGL - Pnut')
xlabel('Time(s)')
ylabel('Altitude (m)')
xlim([(min(t)-1), (max(t)+1)])
exportgraphics(gcf, sprintf('%s_altitude_pnut.png', launch), 'Resolution', 600);

figure
plot(t, vel, 'LineWidth', lw, 'Color', col2)
title('Velocity - Pnut')
xlabel('Time(s)')
ylabel('Velocity (m/s)')
xlim([(min(t)-1), (max(t)+1)])
exportgraphics(gcf, sprintf('%s_velocity_pnut.png', launch), 'Resolution', 600);

figure
plot(t, temp, 'LineWidth', lw, 'Color', col3)
title('Temperature - Pnut')
xlabel('Time(s)')
ylabel('Velocity (m/s)')
xlim([(min(t)-1), (max(t)+1)])
exportgraphics(gcf, sprintf('%s_temperature_pnut.png', launch), 'Resolution', 600);
