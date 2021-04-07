/**
 * Copyright (c) 2020 Raspberry Pi (Trading) Ltd.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 */

#include <stdio.h>
#include <stdlib.h>

#include <Arduino.h>
#include "pico/stdlib.h"
#include "hardware/flash.h"

// We're going to erase and reprogram a region 256k from the start of flash.
// Once done, we can access this at XIP_BASE + 256k.
#define FLASH_TARGET_OFFSET (256 * 1024)

const uint8_t *flash_target_contents = (const uint8_t *) (XIP_BASE + FLASH_TARGET_OFFSET);

void print_buf(const uint8_t *buf, size_t len) {
    for (size_t i = 0; i < len; ++i) {
        Serial.print(buf[i], HEX);
        if (i % 16 == 15)
            Serial.print("\n");
        else
            Serial.print(" ");
    }
}

void setup() {
    Serial.begin();
    pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    Serial.println("hello");
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    delay(1000);
    static uint8_t random_data[FLASH_PAGE_SIZE];
    for (int i = 0; i < FLASH_PAGE_SIZE; ++i)
        random_data[i] = rand() >> 16;

    Serial.println("Generated random data:");
    print_buf(random_data, FLASH_PAGE_SIZE);

    // Note that a whole number of sectors must be erased at a time.
    // Serial.println("Erasing target region...");
    // flash_range_erase(FLASH_TARGET_OFFSET, FLASH_SECTOR_SIZE);
    // Serial.println("Done. Read back target region:");
    // print_buf(flash_target_contents, FLASH_PAGE_SIZE);

    Serial.println("\nProgramming target region...");
    flash_range_program(FLASH_TARGET_OFFSET, random_data, FLASH_PAGE_SIZE);
    Serial.println("Done. Read back target region:");
    print_buf(flash_target_contents, FLASH_PAGE_SIZE);

    // bool mismatch = false;
    // for (int i = 0; i < FLASH_PAGE_SIZE; ++i) {
    //     if (random_data[i] != flash_target_contents[i])
    //         mismatch = true;
    // }
    // if (mismatch)
    //     Serial.println("Programming failed!");
    // else
    //     Serial.println("Programming successful!");
    // delay(1000);
}