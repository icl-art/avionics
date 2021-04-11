clear

col1 = '#2978a0';
col2 = '#BA1200';
col3 = '#3EC300';
G = 9.8065;

data = readmatrix('astra.csv');

t = data(:, 1);
pressure = data(:, 2);
temp = data(:, 3);
acc_x = data(:, 4)*G;
acc_y = data(:, 5)*G;
acc_z = data(:, 6)*G;
g_x = data(:, 7);
g_y = data(:, 8);
g_z = data(:, 9);

t = t/1000;

figure
hold on
plot(t, temp, 'LineWidth', 1, 'Color', col1)
title('Temperature');
xlabel('Time(s)');
ylabel('Temperature (C)');
xlim([(min(t)-1), (max(t)+1)])
hold off

figure
title('Acceleration');
xlabel('Time (s)')
ylabel('Acceleration (m/s^2)')
hold on
plot(t, acc_x, 'LineWidth', 1, 'Color', col1)
plot(t, acc_y, 'LineWidth', 1, 'Color', col2)
plot(t, acc_z, 'LineWidth', 1, 'Color', col3)
legend('x', 'y', 'z')
xlim([(min(t)-1), (max(t)+1)])

figure
title('Angular Velocity');
xlabel('Time (s)')
ylabel('Gyro (rad/s)')
hold on
plot(t, g_x, 'LineWidth', 1, 'Color', col1)
plot(t, g_y, 'LineWidth', 1, 'Color', col2)
plot(t, g_z, 'LineWidth', 1, 'Color', col3)
legend('x', 'y', 'z')
xlim([(min(t)-1), (max(t)+1)])
hold off

height = atmospalt(pressure);

figure
hold on
title('Pressure/Altitude Plot')
xlabel('Time(s)')

yyaxis left
plot(t, pressure, 'LineWidth', 1, 'Color', col1)
ylabel('Pressure (Pa)')

yyaxis right
plot(t, height, 'LineWidth', 1, 'Color', col2)
ylabel("Altitude ASL (m)")

xlim([(min(t)-1), (max(t)+1)])


