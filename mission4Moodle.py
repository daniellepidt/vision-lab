import cv2,numpy as np

class Config_Pic():


    # Build trackbar from list of attributes names for configuration of network video.

    # Parameters 3 lists:

    #     names: names of attributes of cam.

    #     values: current value of attribute

    #     counts: max values of attributes


    def __init__(self,**dict):

        '''

            # Creates trackbars for all desired attributes.

            # :argument

        '''

        # Names of trackbars.


        # Initial values of trackbars.


        # Max values of trackbars.


        # Define window for trackbars.


        # Loop over names list


            # Create trackbars



    # Define callback for the trackbars

    def on_track(self,x):

        # All computation done in main so we pass it.




    def printVals(self,dic):

        '''

            # Print real values of parameters.

            # :argument Dictionary of values


        '''

        # Loop through all keys and values of dictionary.


            # If key is 'Beta'


                # Print values


            # If alpha or gamma


                # Print values devided by 100.



    def main(self):

        '''

            # Changes video appearance according to user trackbars preferences

            #

            # :argument


        '''

        # Capture video


        # Define dictionary.


        # Do forever


            # Read video


            # If no frame (or video ended)


                # Print values of attributes


                # Break infinite loop


            # If user escaped.


                # Print values of attributes


                # Break infinite loop


            # Loop through list of names


                # Assign dic attribute name as key trackbar value as value


            ###################

            # Code for Gamma correction

            # Define a lookup table of all intensities (0-255)


            # Loop all table values


                # Populate the table


            # Constract image with new gamma correction values.


            # End Gamma correction code

            #####################

            # Scale img by 2


            # Constract image with new Alpha and Beta correction values.


            # Show the new image





