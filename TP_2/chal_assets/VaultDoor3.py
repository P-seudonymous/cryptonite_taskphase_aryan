str = 'jU5t_a_sna_3lpm18g947_u_4_m9r54f'
buffer = [''] * 32

for i in range(31,16,-2):
    buffer[i] = str[i]

for i in range(16, 32, 2):
    buffer[i] = str[46 - i]
    
for i in range(8, 16):
    buffer[i] = str[23-i]

for i in range(8):
    buffer[i] = str[i]


print(''.join(buffer))
