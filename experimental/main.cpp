#include <stdio.h>
#include <stdlib.h>

#include "pico/stdlib.h"
#include "hardware/flash.h"
#include "hardware/uart.h"
#include "hardware/gpio.h"

#define DEBUG 1

// We're going to erase and reprogram a region 256k from the start of flash.
// Once done, we can access this at XIP_BASE + 256k.
#define FLASH_TARGET_OFFSET (256 * 1024)

const uint8_t *flash_target_contents = (const uint8_t *)(XIP_BASE + FLASH_TARGET_OFFSET);

const uint LED_PIN = PICO_DEFAULT_LED_PIN;

#define UART_ID uart0
#define BAUD_RATE 9600

// We are using pins 0 and 1, but see the GPIO function select table in the
// datasheet for information on which other pins can be used.
#define UART_TX_PIN 16
#define UART_RX_PIN 17

#define BUTTON_PIN 28

void blink(const int, const int);
void wait(const int);

int main()
{
    // Set up our UART with the required speed.
    uart_init(UART_ID, BAUD_RATE);

    // Set the TX and RX pins by using the function select on the GPIO
    // Set datasheet for more information on function select
    gpio_set_function(UART_TX_PIN, GPIO_FUNC_UART);
    gpio_set_function(UART_RX_PIN, GPIO_FUNC_UART);

    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);
    gpio_init(BUTTON_PIN);
    gpio_set_dir(BUTTON_PIN, GPIO_IN);

    gpio_put(LED_PIN, 1);
    int i = 0;
    wait(28);
    uart_puts(UART_ID, "hello\r\n");
    gpio_put(LED_PIN, 0);


//    blink(500, 5);
    uint8_t random_data[FLASH_PAGE_SIZE];
    for (int i = 0; i < FLASH_PAGE_SIZE; ++i)
        random_data[i] = rand() >> 16;

    uart_puts(UART_ID, "Generated data\r\n");

    flash_range_erase(FLASH_TARGET_OFFSET, FLASH_SECTOR_SIZE); //Erases 4096 bytes at a time

    uart_puts(UART_ID, "Erased flash\r\n");

    flash_range_program(FLASH_TARGET_OFFSET, random_data, FLASH_PAGE_SIZE);

    uart_puts(UART_ID, "Programmed flash\r\n");

    bool mismatch = false;
    for (int i = 0; i < FLASH_PAGE_SIZE; ++i)
    {
        if (random_data[i] != flash_target_contents[i])
            mismatch = true;
    }
    if (mismatch)
        uart_puts(UART_ID, "Programming failed!\r\n");
    else
        uart_puts(UART_ID, "Programming successful!\r\n");

    while (1)
    {
        uart_puts(UART_ID, "Hello world\r\n");
        sleep_ms(1000);
    }
}

void blink(const int delay, const int n)
{
    for (int i = 0; i < n; i++)
    {
        gpio_put(LED_PIN, 1);
        sleep_ms(delay);
        gpio_put(LED_PIN, 0);
        sleep_ms(delay);
    }
}

void wait(const int pin) {
    while (!gpio_get(pin)) {
        uart_puts(UART_ID, "waiting...\n\r");
        sleep_ms(500);
    }
}