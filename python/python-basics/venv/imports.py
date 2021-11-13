import world
world
world.africa
from world import europe
europe.greece
world.europe.norway

# The spain submodule has not been imported
# europe.spain

# Import spain explicitly inside the world namespace
import world.europe.spain
# Note that spain is also available directly inside the europe namespace
europe.spain
# Importing norway doesn't do the import again (no output), but adds
# norway to the global namespace
from world.europe import norway
norway

# Even though africa has been imported, zimbabwe has not
#world.africa.zimbabwe


# Import zimbabwe explicitly into the global namespace
from world.africa import zimbabwe

# The zimbabwe submodule is now available
zimbabwe

# Note that zimbabwe can also be reached through the africa subpackage
world.africa.zimbabwe