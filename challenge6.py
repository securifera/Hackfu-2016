postion = 640, 640 
size = 320 , 320 
center = 800, 800

image = gimp.image_list()[0]
drw=pdb.gimp_image_get_active_layer(image)

size = 340
coords = 630

while coords > -1:
 pdb.gimp_rect_select(image,coords,coords,size,size,2,0,0)
 pdb.gimp_rotate(drw,0,-3.14159/2)
 flt_sel = pdb.gimp_image_floating_selection (image)
 pdb.gimp_floating_sel_anchor(flt_sel)
 size += 20
 coords -= 10