############ INSTRUCTIONS ##############
########################################

#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

#Find two lines that together with the x-axis form a container, such that the container contains the most water.

#Return the maximum amount of water a container can store.

#Notice that you may not slant the container.

############### EXERCISE ###############
########################################

def maxArea(self, height):
    left, right = 0, len(height)-1
    water_max = -1

    while left < right:
        water_held = min(height[left],height[right]) * (right-left)

        if water_held > water_max:
            water_max = water_held
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return water_max