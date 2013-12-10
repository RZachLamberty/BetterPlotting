import scipy, pylab
import matplotlib.colors as mplColors
import matplotlib.cm as mplColorMap



#########################################
#   Some colormap creation functions    #
#########################################

def colorListToMap( colorList, colorMapName, gradation = 1024 ):
    """
    Given a list of colors (more than one) in rgb form, create a linear
    segmented color map named colorMapName with gradation number of different
    values
    """
    colorKeyList = ['red', 'green', 'blue']
    colorMapDic = {}    
        
    for i in range( len( colorList ) ):
        pivotPoint = i / ( len( colorList ) - 1. )
        rgbColor = colorList[i]
        if len( rgbColor ) != 3:
            raise ValueError, "Probably not an RGB color list"
        for j in range(3):
            colorKey = colorKeyList[j]
            if colorKey not in colorMapDic:
                colorMapDic[ colorKey ] = []
            colorMapDic[ colorKey ].append( (pivotPoint, rgbColor[j], rgbColor[j]) )
    
    return mplColors.LinearSegmentedColormap( colorMapName, colorMapDic, gradation )


def viewColorMap( colorMapList ):
    """
    Given a single color map, view it in action
    """
    a = scipy.outer( scipy.arange(0,1,0.01), scipy.ones(10) )
    pylab.figure( figsize = (10,5) )
    pylab.subplots_adjust( top = 0.8, bottom = 0.05, left = 0.01, right = 0.99)
    
    l = len( colorMapList ) + 1
    for i, m in enumerate( colorMapList ):
        pylab.subplot( 1, l, i+1)
        pylab.axis("off")
        pylab.imshow( a, aspect = 'auto', cmap = m, origin = "lower")
        pylab.title( m.name, rotation = 90, fontsize = 10)
    
    pylab.show()


def sinContours( colorMap, N = 25):
    """
    Given a color map, plot the sine contour function
    """
    x = scipy.arange( 0, 6*scipy.pi, 6*scipy.pi / 250. )
    y = scipy.arange( 0, 6*scipy.pi, 6*scipy.pi / 250. )
    z = scipy.array( [ [ scipy.sin(xi) * scipy.sin(yj) for yj in y ] for xi in x ] )
    
    pylab.contourf( x, y, z, N, cmap = colorMap )
    
    pylab.xlim( 0, 6*scipy.pi )
    pylab.ylim( 0, 6*scipy.pi )
    pylab.colorbar()
    

def sinPlots( colorList ):
    """
    Given a color map, plot several sin functions (to display the different
    colors in the color cycle
    """
    fig = pylab.figure()
    ax = fig.add_subplot(111)
    ax.set_color_cycle( colorList )
    
    x = scipy.arange( 0, 6*scipy.pi, 6*scipy.pi / 250. )
    
    for i in range(10):
        
        ax.plot( x, scipy.sin( x / float(i) ), label = str(i), linewidth = 3)
    
    pylab.show()
    

#############################
#   A basic ROYGBIV set     #
#############################

#   Some basic triadic colors
LIGHT_BLUE = '#19AFFF'
GOLDENROD = '#FFF800'
CORNELL_RED = '#B20915'
BASE_COLORS = [LIGHT_BLUE, GOLDENROD, CORNELL_RED]

#   Their compliments
SOFT_ORANGE = '#FF8F00'
SOLID_PURPLE = '#4A00B2'
CHRISTMAS_GREEN = '#00B22B'
COMPLIMENT_COLORS = [SOFT_ORANGE, SOLID_PURPLE, CHRISTMAS_GREEN]

#   The "split the difference" triadic colors
BRIGHT_ORANGE = '#FF9E00'
ROYAL_PURPLE = '#6609B2'
LIGHT_GREEN = '#00FF62'
SPLIT_COLORS = [BRIGHT_ORANGE, ROYAL_PURPLE, LIGHT_GREEN]

#   Some lists, purple to red
HEX_COLOR_LIST_1 = [SOLID_PURPLE, LIGHT_BLUE, CHRISTMAS_GREEN, GOLDENROD, SOFT_ORANGE, CORNELL_RED]
HEX_COLOR_LIST_2 = [ROYAL_PURPLE, LIGHT_BLUE, LIGHT_GREEN, GOLDENROD, BRIGHT_ORANGE, CORNELL_RED]
RGB_COLOR_LIST_1 = [ mplColors.hex2color( htmlColor ) for htmlColor in HEX_COLOR_LIST_1 ]
RGB_COLOR_LIST_2 = [ mplColors.hex2color( htmlColor ) for htmlColor in HEX_COLOR_LIST_2 ]

zachColorMap1 = colorListToMap( RGB_COLOR_LIST_1, 'zachColorMap1' )
zachColorMap2 = colorListToMap( RGB_COLOR_LIST_2, 'zachColorMap2' )

#   For the record, I think map 2 is prettier.



#################################
#   A 'special colors' set      #
#################################

OCTOBER_PURPLE = '#662845'
OCTOBER_GREEN = '#577867'
OCTOBER_YELLOW = '#EDCE82'
OCTOBER_ORANGE = '#D68644'
OCTOBER_RED = '#AB3229'
OCTOBER_HEX_COLORS = [OCTOBER_PURPLE, OCTOBER_GREEN, OCTOBER_YELLOW, OCTOBER_ORANGE, OCTOBER_RED]
OCTOBER_RGB_COLORS = [ mplColors.hex2color( htmlColor ) for htmlColor in OCTOBER_HEX_COLORS ]

octoberColorMap = colorListToMap( OCTOBER_RGB_COLORS, 'october' )


#########################
#   Solid colors set    #
#########################

SOLID_PURPLE = '#530066'
SOLID_BLUE = '#000452'
SOLID_CYAN = '#2DB2AE'
SOLID_GREEN = '#005418'
SOLID_YELLOW = '#FFFF0D'
SOLID_ORANGE = '#FF5900'
SOLID_MAROON = '#590000'
SOLID_HEX_COLORS = [ SOLID_PURPLE, SOLID_BLUE, SOLID_CYAN, SOLID_GREEN, SOLID_YELLOW, SOLID_ORANGE, SOLID_MAROON ]
SOLID_RGB_COLORS = [ mplColors.hex2color( htmlColor ) for htmlColor in SOLID_HEX_COLORS ]

solidColorMap = colorListToMap( SOLID_RGB_COLORS, 'solid' )


#############
#   Bright  #
#############

BRIGHT_PURPLE = '#9754E8'
BRIGHT_INDIGO = '#AB41FF'
BRIGHT_BLUE = '#5CC0FF'
BRIGHT_GREEN = '#00FF48'
BRIGHT_YELLOW = '#FFFC40'
BRIGHT_ORANGE = '#FFB042'
BRIGHT_RED = '#FF0000'
BRIGHT_HEX_COLORS = [ BRIGHT_PURPLE, BRIGHT_INDIGO, BRIGHT_BLUE, BRIGHT_GREEN, BRIGHT_YELLOW, BRIGHT_ORANGE, BRIGHT_RED ]
BRIGHT_RGB_COLORS = [ mplColors.hex2color( hexColor ) for hexColor in BRIGHT_HEX_COLORS ]

brightColorMap = colorListToMap( BRIGHT_RGB_COLORS, 'bright' )



#################
#   PASTELS     #
#################

PASTEL_PURPLE = '#CCBCE8'
PASTEL_BLUE = '#9B94FF'
PASTEL_CYAN = '#B2E8DA'
PASTEL_GREEN = '#8BFFC5'
PASTEL_ORANGE = '#FFF6BF'
PASTEL_BROWN = '#E8C090'
PASTEL_YELLOW = '#FEFFA8'
PASTEL_PINK = '#FFB0E3'
PASTEL_RED = '#FF978B'

PASTEL_HEX_COLORS = [ PASTEL_PURPLE, PASTEL_BLUE, PASTEL_CYAN, PASTEL_GREEN, PASTEL_ORANGE, PASTEL_BROWN, PASTEL_YELLOW, PASTEL_PINK, PASTEL_RED ]
PASTEL_RGB_COLORS = [ mplColors.hex2color( hexColor ) for hexColor in PASTEL_HEX_COLORS ]

pastelColorMap = colorListToMap( PASTEL_RGB_COLORS, 'pastel' )
