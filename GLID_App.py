# import libraries
from dataclasses import dataclass
import streamlit as st

@dataclass
class Gas_Lift:
    """
    This class contains the methods for evaluating the feasibility of Gas Lift installation.
    """

    def Production_Data(self, productivity_index: str, Bottomhole_pressure: str, Gas_Liquid_Ratio: str) -> int:
        """
        This method evaluates the feasibility of Gas Lift installation based on production data.

        Args:
            productivity_index (str): The Productivity Index description of the well.
            Bottomhole_pressure (str): The Bottomhole reservoir pressure description of the well.
            Gas_Liquid_Ratio (str): The Gas Liquid Ratio description of the well.

        Returns:
            int: A binary value (0 or 1) representing feasibility of Gas Lift installation based on the production data.
        """
        if productivity_index in ('High', 'Low') and Bottomhole_pressure in ('High', 'Low') and Gas_Liquid_Ratio == 'High':
            return 1
        else:
            return 0

    def Economic_Data(self, gas_availability: str, compression_costs: str) -> int:
        """
        This method evaluates the feasibility of Gas Lift installation based on economic feasibility data.

        Args:
            gas_availability (str): The gas availability description.
            compression_costs (str): The compression cost availability description.

        Returns:
            int: A binary value (0 or 1) representing feasibility of Gas Lift installation based on economic feasibility data.
        """
        if gas_availability == 'Yes' and compression_costs == 'Available':
            return 1
        else:
            return 0

    def Environmental_Data(self, environmental_impact: str) -> int:
        """
        This method evaluates the feasibility of Gas Lift installation based on environmental impact data.

        Args:
            environmental_impact (str): The environmental impact description.

        Returns:
            int: A binary value (0 or 1) representing feasibility of Gas Lift installation based on environmental impact data.
        """
        if environmental_impact == 'Positive':
            return 1
        else:
            return 0


#####################################################################################################################
""" Streamlit Application """
####################################################################################################################3

# Define column layout for the page
col1, col2, col3 = st.columns([1, 3, 1])

# Set empty space in first and third columns to center the image in the second column
with col1:
    st.write("")

with col2:
    # Display logo image in the center column
    st.image("Gas_Lift_logo.PNG", width=300)

with col3:
    st.write("")

# Create two tabs on the page: "Gas Lift" and "About"
tab1, tab2 = st.tabs(["**Gas Lift**", "**About**"])

# Populate the "Gas Lift" tab with input fields and options
with tab1:
    # Display an image in the sidebar
    st.sidebar.image("GLIDbackground.PNG", width=300)
    st.write("")

    # Add a caption and link to the author's LinkedIn profile in the sidebar
    st.sidebar.caption(
        'Made in 🎈 [Streamlit](https://www.streamlit.io/), by[Praise Ekeopara](https://www.linkedin.com/in/praiseekeopara)')
    st.sidebar.markdown("")

    # Add a heading for the "Production Data" section
    st.write('**Production Data**')

    # Create an expander to contain input fields for the "Production Data" section
    with st.expander("✨ Enter Production Data", expanded=False):
        # Divide the expander into three columns for input fields
        col1, col2, col3 = st.columns(3)

        # Add a selectbox for "Productivity Index" in the first column with a description in the help tooltip
        with col1:
            product_index = st.selectbox(
                "**Productivity Index**",
                ("High", "Low", "None"),
                help="""
                Select the suitable Productivity Index description.
                """,
            )

        # Add a selectbox for "Bottomhole Pressure" in the second column with a description in the help tooltip
        with col2:
            BHP = st.selectbox(
                "**Bottomhole Pressure**",
                ('High', 'Low', 'None'),
                help="""
                Enter the Bottomhole reservoir pressure description of the well.
                """,
            )

        # Add a selectbox for "Gas Liquid Ratio" in the third column with a description in the help tooltip
        with col3:
            GLR = st.selectbox(
                "**Gas Liquid Ratio**",
                ('High', 'Low', 'None'),
                help="Select suitable Gas Liquid Ratio description",
            )

    # Add a heading for the "Economic feasibility Data" section
    st.write('**Economic feasibility Data**')
    # Create an expander to contain input fields for the "Economic feasibility Data" section
    with st.expander("✨ Enter Economic feasibility Data", expanded=False):
        # Divide the expander into two columns for input fields
        col1, col2 = st.columns(2)

        # Add a selectbox for "Gas availability" in the first column with a description in the help tooltip
        with col1:
            gas_available = st.selectbox(
                "**Gas availability**",
                ("Yes", "No"),
                help="""
                Select the gas availability.
                """,
            )
            # Add a selectbox for "Compression cost" in the second column with a description in the help tooltip
        with col2:
            compression_costs_ = st.selectbox(
                "**Compression cost**",
                ("Available", "Not Available"),
                help='''
                    Select the compression cost availability''')

    # Add a heading for the "Environmental impact Data" section
    st.write('**Environmental impact Data**')
    # Add an expander widget to allow the user to enter environmental impact data
    with st.expander("✨ Enter Environmental impact Data", expanded=False):

        # Create a column to contain the selectbox widget
        col1, = st.columns(1)

        # Add the selectbox widget to the column
        with col1:
            impact = st.selectbox(
                "**Environmental impact**",
                ("Positive", "Negative"),
                help='Select the suitable environmental impact of the project.',
            )

    # Create an instance of the Gas_Lift class
    gas_lift = Gas_Lift()

    # Calculate the production, economic, and environmental data based on the input
    production_data = gas_lift.Production_Data(product_index, BHP, GLR)
    economic_data = gas_lift.Economic_Data(gas_available, compression_costs_)
    environmental_data = gas_lift.Environmental_Data(impact)

    # Create a list of the calculated data
    general_decision_list = [production_data, economic_data, environmental_data]

    # Find the most common item in the list
    most_common = max(set(general_decision_list), key=general_decision_list.count)

    # Create two columns to display the recommendation and a button to trigger the recommendation
    col1, col2 = st.columns(2)

    # Add a button to trigger the recommendation
    with col1:
        if st.button(label="Recommend", help='Click to recommend Well Gas lift or not'):
            if economic_data == 0:
                col2.write('<span style="color: red;">**Do not Gas lift the well!**</span>',
                           unsafe_allow_html=True)
            # Display a recommendation based on the most common item in the list
            elif most_common == 1:
                col2.write('<span style="color: red;">**Gas lift the well!**</span>',
                           unsafe_allow_html=True)
            elif most_common == 0:
                col2.write('<span style="color: red;">**Do not Gas lift the well!**</span>',
                           unsafe_allow_html=True)
            else:
                col2.write('<span style="color: red;">**Check information entered!**</span>', unsafe_allow_html=True)

# Describes the Software in the 'About' section
with tab2:
    st.write("## Welcome to GLID! 👋")

    st.markdown(
        """
        **GLID** is a **G**as **L**ift **I**nstallation **D**ecision-making software, designed for Production and other 
        Energy experts for faster and reliable decision making on whether to Gas lift a well or not. 

        It's credibility is attributed to it's vast factor considerations leveraging various information of the well 
        such as; 

        1. Reservoir Characteristics
        2. Production information
        3. Environmental impact information
        4. Economic feasibility information

        Enjoy the decision making power of **GLID** with a simple click on the "**Recommend**" button !


        ### Have a demo today!
        """)
