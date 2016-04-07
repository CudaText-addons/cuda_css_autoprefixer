Plugin "CSS AutoPrefixer" for CudaText.
It allows to insert needed vendor prefixes into CSS code.
Uses Node.js library "Autoprefixer". 
If selection is made (only normal selection supported) then only selection is changed,
otherwise entire file is changed.
Plugin has commands in "Plugins" menu. 

Example

Such CSS code:

    #wrapper {
        border-radius: 1em;
        transform: rotate(45deg)
    }

will be changed to:

    #wrapper {
        border-radius: 1em;
        -webkit-transform: rotate(45deg);
            -ms-transform: rotate(45deg);
                transform: rotate(45deg)
    }


Author: Alexey T.
License: MIT
