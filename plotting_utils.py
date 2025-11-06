import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio


# setting up a style function for my seaborn plots
def sns_plot_setup(style='dark_background', palette='crest', size=(12,7)): 
    """This Function sets up the style for every seaborn plot in the File.
    
    Args:
      style (str): sets the standard style. default='dark background' (or use: 'classic', 'default', 'ggplot',...)
      palette (str): sets the standard color palette, default='crest' (or use: 'viridis', 'magma', 'plasma','deep', 'muted',...)
      size(tuple): determines the size of the plots

    Returns:
        None
    """ 
    # setting dark background
    plt.style.use(style)
    
    # setting a global color palette
    sns.set_palette(palette)

    # setting up standard size
    plt.rc('figure', figsize=size)
    
    # setting up a grid for visibility
    plt.rc('grid', color='#cccccc', linewidth=0.8, linestyle='--', alpha=0.3)

    # setting up standard font-size
    plt.rc('font', family='Consolas', size=12)
    plt.rc('axes', titlesize=18, labelsize=14)
    plt.rc('xtick', labelsize=12)
    plt.rc('ytick', labelsize=12)
    plt.rc('legend', fontsize=12)


# setting up a stzle function for my plotly express plots
def px_plot_setup(template='plotly_dark'):
    """This function sets up the style for every px plot in the file. 
    
    Args:
      template (str): sets the standard template for all px-plots. default='plotly_dark' (or use:'ggplot2', 'seaborn', 'plotly_white')

    Returns:
      None
    """
    # changing the font to Consolas
    if template in pio.templates:
        pio.templates[template].layout.font.family = 'Consolas'
    else:
        print(f"Warning: Plotly template '{template}' wasn't found. Font not set.")
    # setting up standard font-size
        pio.templates[template].layout.font.size = 12
    # setting the template as default    
    pio.templates.default = template
    