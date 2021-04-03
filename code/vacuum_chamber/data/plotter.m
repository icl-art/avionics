clear

calib = 102800;

data1 = readmatrix('pnut1.csv');
data2 = readmatrix('pnut2.csv');

% data1 = readmatrix('vactest1.csv');
% data2 = readmatrix('vactest2.csv');
% data3 = readmatrix('vactest3.csv');
% data4 = readmatrix('pnut1.csv');
% data5 = readmatrix('pnut2.csv');

col1 = '#1B2CC1';
col2 = '#C14953';
col3 = '#2292A4';
col4 = '#FF9000';


figure
hold on

plot(data1(:, 1), data1(:, 2), 'Color', col1, 'LineWidth', 1)
plot(data2(:, 1), data2(:, 2), 'Color', col2, 'LineWidth', 1)
% plot(data3(:, 1), data3(:, 2), 'Color', col3, 'LineWidth', 1)
% plot(data4(:, 1), data4(:, 2), 'Color', col1, 'LineWidth', 1)
% plot(data5(:, 1), data5(:, 2), 'Color', col2, 'LineWidth', 1)

title('Pressure/time plot for vacuum "chamber"')
xlabel('time (s)')
ylabel ('Pressure (Pa)')
legend('Run 1', 'Run 2', 'Location', 'best')


heights = atmospalt([calib min(data1(:, 2)) min(data2(:, 2))]);

deltah1 = heights(2) - heights(1);
deltah2 = heights(3) - heights(1);
% deltah3 = heights(4) - heights(1);

lab1 = sprintf ('Altitude achieved in run 1 was %.1f ft\n', deltah1/0.3);
lab2 = sprintf ('Altitude achieved in run 2 was %.1f ft\n', deltah2/0.3);

% fprintf ('Altitude achieved in run 3 was %.1f ft', deltah3/0.3);
% text((data1(find(data1(:, 2) == min(data1(:, 2))))), min(data1(:, 2)), lab1);
outcome = {lab1, lab2};
dim = [0.15 0.3 0.3 0.3];
annotation('textbox', dim, 'String', outcome, 'FitBoxToText', 'off');
exportgraphics(gcf, 'testing-16mar.png', 'Resolution', 600);