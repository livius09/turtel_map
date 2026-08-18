you know like javaFX but just in shity and in python

### Made this shit in like 2 days on company time

idea is to use inheretance

then to have:
-lable
-button
-textfield
-sprite

-radio button
-drop down

-VBOX
-HBOX
-Scene

### general
there is always one scene renderd but you can build others and swap them out
event driven only update when something changed
also only redraws when something is dirty
when something needs animation it gets put into a special list
wehre it gets a tick 
has a selected field for where keyboard inputs go to
all functions always recive the turtle whit penup
position is left down


### Base
-x
-y
-Heigh
-width
-outline
-dirty
-color

callbacks:
-on clicked
-on hover


this is the base obj all the others inherit from


#### lable
-text
-fontsize

just a normal textfield
displays text
font size can be configured


### button
is a lable
but you know a bit special
can tab into

-outline
-click animation

a dedicated class for interactivity which natively has an outline
plays like a small animation when clicked 

#### textfield
prob the most dificult one
blinking cursor when selected displaying
can tab into

-infotext
-text


#### sprite
-arr_shape

for showing special shapes 
to be drawn

#### BOX
-nodes

boxes space out all theyr elements based on space avavible
Vbox does it vertical
Hbox does it horizontaly

#### scene
-nodes

a scene can be built whitout showing and then swaped in as a sub menu ect
