CC = gcc
CFLAGS = -O2 -Wall -Wextra -std=c11
AR = ar
ARFLAGS = rcs

LIB = libfibonacci.a              
OBJS = fibonacci_Library.o        
EXE = fibonacci_demo             


all: $(LIB) $(EXE)


$(LIB): $(OBJS)
	$(AR) $(ARFLAGS) $@ $^


fibonacci_Library.o: fibonacci_Library.c fibonacci_Library.h
	$(CC) $(CFLAGS) -c fibonacci_Library.c -o fibonacci_Library.o


$(EXE): main.c $(LIB)
	$(CC) $(CFLAGS) main.c -L. -lfibonacci -o $(EXE)


clean:
	rm -f $(OBJS) $(LIB) $(EXE)
