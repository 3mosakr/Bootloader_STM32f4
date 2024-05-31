# Bootloader_STM32f4 and Self Programming

simple Bootloader for STM32f401CC.

Project Description:
  the bootloader folder include the Bootloader code (use the Flasher/Debugger to burn this code into MCU FLASH)
  then you use the USB to TTL to burn the new code using (USART Communication Protocol) -> use the Python script to send the data through your port. 

  in the Python script choose your serial port for example (COM4, COM5, ...) and (File path).

  The another folder (bootloader App) is Test Project Code to test the self programming concept.
  

  
