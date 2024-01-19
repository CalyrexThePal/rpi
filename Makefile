# Compiler to use
CC=gcc

# Compiler flags
CFLAGS=-Wall

# Target executable name
TARGET=rpi_adc_dma_test

# Source files
SRCS=rpi_adc_dma_test.c rpi_dma_utils.c

# Object files (replace .c from SRCS with .o)
OBJS=$(SRCS:.c=.o)

# Default target
all: $(TARGET)

# Rule to link the program
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJS)

# Rule to compile the source files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Rule for cleaning up
clean:
	rm -f $(TARGET) $(OBJS)

# Rule to run the program (requires sudo)
run: $(TARGET)
	sudo ./$(TARGET)