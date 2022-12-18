section .data
  mass dd 938.3
  charge dd 1
  spin dd 0.5
  particles dd 0
  EXTERN create_particle


section .text
  global _start

_start:
  ; Iterate over the particles in the diagram
  mov eax, [mass]
  mov ebx, [charge]
  mov ecx, [spin]
  
  mov eax, [mass]
  mov ebx, [charge]
  mov ecx, [spin]
  mov eax, [mass]
  mov ebx, [charge]
  mov ecx, [spin]
  call Annihilate
  call Create
  call Scatter
  add eax, 5
  sub eax, 10
  add ebx, 15

  int 0x80

; Define the functions called by the call instructions
Annihilate:
  ; Add your code here
  ret

Create:
  ; Check if there are at least two particles in the list
  mov eax, [particles]
  mov eax, [eax]
  cmp eax, 2
  jae end_create

  ; Get the two particles involved in the interaction
  mov eax, [particles]
  mov eax, [eax]
  dec eax
  mov ebx, [particles + eax*4]
  dec eax
  mov ecx, [particles + eax*4]

  ; Remove the particles from the list of particles
  mov edx, [particles]
  mov edx, [edx]
  mov [particles + eax*4], ebx
  dec edx
  mov [particles + eax*4], ecx
  dec edx
  mov [particles], edx
  
  ; Create a new particle
  mov [rsp-8], ecx
  mov [rsp-4], ebx
  call create_particle
  add rsp, 8
  mov [particles], eax

end_create:
  ret

create_particle:
  ; Add your code here
  ret

Scatter:
  ; Add your code here
  ret

Decay:
  ; Add your code here
  ret

PairProduction:
  ; Add your code here
  ret
