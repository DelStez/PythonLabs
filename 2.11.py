word = input()
gl_lass = 'уеыаоэяию'
sg_lass = 'йцкнгшщзхъфвпрлджчсмтьб'
gl = 0 ; sg = 0
for i in word:
    if i in gl_lass:
        gl += 1
    elif i in sg_lass:
        sg += 1
    else:
        i +=1
print("Гласных {}, согласных {}".format(gl, sg))
