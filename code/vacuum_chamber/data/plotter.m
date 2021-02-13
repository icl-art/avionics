clear

data1 = readmatrix('vactest1.csv');
data2 = readmatrix('vactest2.csv');
data3 = readmatrix('vactest3.csv');

col1 = '#1B2CC1';
col2 = '#C14953';
col3 = '#2292A4';
col4 = '#FF9000';


figure
hold on

plot(data1(:, 1), data1(:, 2), 'Color', col1, 'LineWidth', 1)

plot(data3(:, 1), data3(:, 2), 'Color', col2, 'LineWidth', 1)

title('Pressure/time plot for vacuum "chamber"')
xlabel('time (s)')
ylabel ('Pressure (Pa)')
legend('Run 1 - box', 'Run 2 - cardboard box', 'Location', 'best')
exportgraphics(gcf, 'testing-13feb.png', 'Resolution', 600);
