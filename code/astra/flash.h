#ifndef FLASH_H
#define FLASH_H

#define PAGE_SIZE 256 //TODO: verify this
void write_buffer(void* buffer, int size);

#endif /* FLASH_H */