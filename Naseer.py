import streamlit as st 

header = st.container()
header.title("Wrap Yourself in Comfort at Night")
header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)

### Custom CSS for the sticky header
st.markdown(
    """
<style>
    div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
        position: sticky;
        top: 2.875rem;
        background-color: white;
        z-index: 999;
    }
    .fixed-header {
        border-bottom: 3px solid black;
    }
</style>
    """,
    unsafe_allow_html=True
) 
  
### Custom CSS for the backgound  
def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://img.freepik.com/premium-photo/white-flowers-leaves-paper-texture-white-background_997580-448.jpg");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack_url() 

### font 
new_title = '<p style="font-family:Forte;text-align: center; color:DarkRed; font-size: 80px;">UK GARMENT</p>'
st.markdown(new_title, unsafe_allow_html=True)
new_title = '<p style="font-family:Viner Hand ITC;text-align: center; color:black; font-size: 50px;">NIGHT WEARS</p>'
st.markdown(new_title, unsafe_allow_html=True)
#st.markdown('# :blue[UK GARMENT]')
#st.subheader(':BLACK[Night Wears]',divider='rainbow')
#st.subheader('',divider='rainbow')
 
### Custom CSS for the sidebar background
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background: url("https://images.pexels.com/photos/7291868/pexels-photo-7291868.jpeg");
        background-size: cover    
    }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    fabric= st.multiselect('FABRIC TYPE',('cotton','pure cotton','alpine','rayon','swiss'))
    st.divider()
    pattern= st.selectbox('PATTERN',('A-line','Plates','Gown'))
    st.divider()
    quality= st.radio('QUALITY',('Normal','Premium'))


tab1, tab2, tab3 = st.tabs([" COLLECTIONS :dress:  ","  ORDER :basket: ", "  CUSTOMER REVIEW :smile:/:pensive:"])
with tab2:
      new_title = '<p style="font-family:Copperplate Gothic Bold;text-align: center; color:GREEN; font-size: 30px;">TO MAKE AN ORDER NOW, FILL YOUR DETAILS HERE !</p>'
      st.markdown(new_title, unsafe_allow_html=True)
      st.text_input('FULL NAME :')
      st.text_area('ADDRESS :')
      st.number_input('PHONE NO. :')
      st.text_area('ORDER NO. (given at bottom of image):')
      st.number_input('QUANTITY :')
      st.divider()
      st.selectbox('WHEN YOU LIKE TO CATCH IT',('TODAY', 'TOMORROW', 'DAY AFTER TOMORROW'))
      st.time_input('AT WHAT TIME YOU WANT TO DELIVER :')
      pay=st.selectbox('PAYMENT METHOD :',('Cash On Delivery','UPI APP'))
      if pay == 'Cash On Delivery':
            st.write('OK')
      if pay == 'UPI APP':
            col1, col2, col3 = st.columns()
            with col2:
                  st.image('QR payment.jpeg') 
      if st.button('SUBMIT'):
            st.write(':red[THANKYOU FOR YOUR PURCHASE ! ] :smile: ')            
            st.write('your order is on its way.')
                 

with tab3:
      st.text_area('Review or Comments:')
      st.slider('RATE OUR SERVICE :', 0, 10, 1)

with tab1:
    if quality == 'Normal':
          if pattern == 'A-line':
                st.write('NORMAL A-LINE NIGHT WEARS')
                st.metric(label='PRICE',value='350 /-')
                if 'cotton' in fabric:
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('Al (3).jpeg')
                            st.metric(label='ORDER NO',value='3')
                      with col2:
                            st.image('Al (4).jpeg')
                            st.metric(label='ORDER NO',value='4')
                      with col3:
                            st.image('Al (7).jpeg')
                            st.metric(label='ORDER NO',value='7')
                      st.divider()
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('Al (5).jpeg')
                            st.metric(label='ORDER NO',value='5')
                      with col2:
                            st.image('Al (10).jpeg')
                            st.metric(label='ORDER NO',value='10')
                      with col3:
                            st.image('Al (11).jpeg')
                            st.metric(label='ORDER NO',value='11')
                      st.divider()             
                if 'pure cotton' in fabric: 
                     col1, col2,col3 = st.columns(3)
                     with col1:
                            st.image('Al (1).jpeg')
                            st.metric(label='ORDER NO',value='1')
                     with col2:
                            st.image('Al (8).jpeg')
                            st.metric(label='ORDER NO',value='8')
                     with col3:
                            st.image('Al (9).jpeg')
                            st.metric(label='ORDER NO',value='9')
                     st.divider()   
                if 'alpine' in fabric:   
                     col1, col2,col3 = st.columns(3)
                     with col1:
                            st.image('Al (13).jpeg')
                            st.metric(label='ORDER NO',value='13')
                     with col2:
                            st.image('Al (14).jpeg')
                            st.metric(label='ORDER NO',value='14')
                     with col3:
                            st.image('Al (15).jpeg')
                            st.metric(label='ORDER NO',value='15')
                     st.divider()        
                if 'swiss' in fabric:
                     col1, col2,col3 = st.columns(3)
                     with col1:
                            st.image('Al (2).jpeg')
                            st.metric(label='ORDER NO',value='2')
                     with col2:
                            st.image('Al (6).jpeg')
                            st.metric(label='ORDER NO',value='6')
                     with col3:
                            st.image('Al (12).jpeg')
                            st.metric(label='ORDER NO',value='12')
                     st.divider()  
          if pattern == 'Plates': 
                st.write('NORMAL NIGHT WEARS WITH PLATES')  
                st.metric(label='PRICE',value='400 /-')    
                if 'cotton' in fabric:
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('Pl (2).jpeg')
                            st.metric(label='ORDER NO',value='2')
                      with col2:
                            st.image('Pl (10).jpeg')
                            st.metric(label='ORDER NO',value='10')
                      with col3:
                            st.image('Pl (15).jpeg')
                            st.metric(label='ORDER NO',value='15')
                      st.divider()            
                if 'pure cotton' in fabric: 
                     col1, col2,col3 = st.columns(3)
                     with col1:
                            st.image('Pl (5).jpeg')
                            st.metric(label='ORDER NO',value='5')
                     with col2:
                            st.image('Pl (7).jpeg')
                            st.metric(label='ORDER NO',value='7')
                     with col3:
                            st.image('Pl (8).jpeg')
                            st.metric(label='ORDER NO',value='8')
                     st.divider()  
                if 'alpine' in fabric:   
                     col1, col2,col3 = st.columns(3)
                     with col1:
                            st.image('Pl (3).jpeg')
                            st.metric(label='ORDER NO',value='3')
                     with col2:
                            st.image('Pl (4).jpeg')
                            st.metric(label='ORDER NO',value='4')
                     with col3:
                            st.image('Pl (9).jpeg')
                            st.metric(label='ORDER NO',value='9')
                     st.divider()  
                     col1, col2,col3 = st.columns(3)
                     with col1:
                            st.image('Pl (6).jpeg')
                            st.metric(label='ORDER NO',value='6')
                     with col2:
                            st.image('Pl (11).jpeg')
                            st.metric(label='ORDER NO',value='11')
                     with col3:
                            st.image('Pl (14).jpeg')
                            st.metric(label='ORDER NO',value='14')
                     st.divider()    
                if 'swiss' in fabric:
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('Pl (1).jpeg')
                            st.metric(label='ORDER NO',value='1')
                      with col2:
                            st.image('Pl (12).jpeg')
                            st.metric(label='ORDER NO',value='12')
                      with col3:
                            st.image('Pl (13).jpeg')
                            st.metric(label='ORDER NO',value='13')
                      st.divider() 

    if quality == 'Premium':
          if pattern == 'A-line':
                st.write('PREMIUM A-LINE NIGHT WEARS')
                st.metric(label='PRICE',value='450 /-')
                if 'alpine' in fabric:
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('A-P (3).jpeg')
                            st.metric(label='ORDER NO',value='3')
                      with col2:
                            st.image('A-P (6).jpeg')
                            st.metric(label='ORDER NO',value='6')
                      st.divider() 
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('A-P (4).jpeg')
                            st.metric(label='ORDER NO',value='4')
                      with col2:
                            st.image('A-P (10).jpeg')
                            st.metric(label='ORDER NO',value='10')
                      with col3:
                            st.image('A-P (18).jpeg')
                            st.metric(label='ORDER NO',value='18')
                      st.divider() 
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('A-P (5).jpeg')
                            st.metric(label='ORDER NO',value='5')
                      with col2:
                            st.image('A-P (8).jpeg')
                            st.metric(label='ORDER NO',value='8')
                      with col3:
                            st.image('A-P (19).jpeg')
                            st.metric(label='ORDER NO',value='19')
                      st.divider() 
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('A-P (7).jpeg')
                            st.metric(label='ORDER NO',value='7')
                      with col2:
                            st.image('A-P (9).jpeg')
                            st.metric(label='ORDER NO',value='9')
                      with col3:
                            st.image('A-P (16).jpeg')
                            st.metric(label='ORDER NO',value='16')
                      st.divider() 
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('A-P (11).jpeg')
                            st.metric(label='ORDER NO',value='11')
                      with col2:
                            st.image('A-P (13).jpeg')
                            st.metric(label='ORDER NO',value='13')
                      with col3:
                            st.image('A-P (15).jpeg')
                            st.metric(label='ORDER NO',value='15')
                      st.divider() 
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('A-P (12).jpeg')
                            st.metric(label='ORDER NO',value='12')
                      with col2:
                            st.image('A-P (14).jpeg')
                            st.metric(label='ORDER NO',value='14')
                      with col3:
                            st.image('A-P (17).jpeg')
                            st.metric(label='ORDER NO',value='17')
                      st.divider() 
                if 'rayon' in fabric:
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('A-P (1).jpeg')
                            st.metric(label='ORDER NO',value='1')
                      with col2:
                            st.image('A-P (22).jpeg')
                            st.metric(label='ORDER NO',value='22')
                      with col3:
                            st.image('A-P (24).jpeg')
                            st.metric(label='ORDER NO',value='24')
                      st.divider() 
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('A-P (2).jpeg')
                            st.metric(label='ORDER NO',value='2')
                      with col2:
                            st.image('A-P (23).jpeg')
                            st.metric(label='ORDER NO',value='25')
                      with col3:
                            st.image('A-P (25).jpeg')
                            st.metric(label='ORDER NO',value='25')
                      st.divider() 
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('A-P (20).jpeg')
                            st.metric(label='ORDER NO',value='20')
                      with col2:
                            st.image('A-P (21).jpeg')
                            st.metric(label='ORDER NO',value='21')
                      st.divider()       
          if pattern == 'Plates':
                st.write('PREMIUM NIGHT WEARS WITH PLATES')
                st.metric(label='PRICE',value='500 /-')
                if 'alpine' in fabric:
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('Pl-P (1).jpeg')
                            st.metric(label='ORDER NO',value='1')
                      with col2:
                            st.image('Pl-P (6).jpeg')
                            st.metric(label='ORDER NO',value='6')
                      with col3:
                            st.image('Pl-P (9).jpeg')
                            st.metric(label='ORDER NO',value='9')
                      st.divider() 
                      ### 56 add
                    
                if 'swiss' in fabric:
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('Pl-P (60).jpeg')
                            st.metric(label='ORDER NO',value='60')
                      st.divider()      
                           
          if pattern == 'Gown':
                st.write('PREMIUM NIGHT WEAR GOWNS')
                st.metric(label='PRICE',value='550 /-')         
                if 'cotton' in fabric:
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('G-P (2).jpeg')
                            st.metric(label='ORDER NO',value='2')
                      st.divider()
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('G-P (4).jpeg')
                            st.metric(label='ORDER NO',value='4')
                      st.divider()    
                if 'alpine' in fabric:
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('G-P (1).jpeg')
                            st.metric(label='ORDER NO',value='1')
                      with col2:
                            st.image('G-P (5).jpeg')
                            st.metric(label='ORDER NO',value='5')
                      with col3:
                            st.image('G-P (15).jpeg')
                            st.metric(label='ORDER NO',value='15')         
                      st.divider()    
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('G-P (7).jpeg')
                            st.metric(label='ORDER NO',value='7')
                      with col2:
                            st.image('G-P (9).jpeg')
                            st.metric(label='ORDER NO',value='9')
                      with col3:
                            st.image('G-P (14).jpeg')
                            st.metric(label='ORDER NO',value='14')         
                      st.divider()    
                if 'rayon' in fabric:
                      col1, col2, col3, col4 = st.columns(4)
                      with col1:
                            st.image('G-P (3).jpeg')
                            st.metric(label='ORDER NO',value='3')
                      with col2:
                            st.image('G-P (6).jpeg')
                            st.metric(label='ORDER NO',value='6')
                      with col3:
                            st.image('G-P (8).jpeg')
                            st.metric(label='ORDER NO',value='8')     
                      with col4:
                            st.image('G-P (13).jpeg')
                            st.metric(label='ORDER NO',value='13')         
                      st.divider()  
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('G-P (10).jpeg')
                            st.metric(label='ORDER NO',value='10')
                      with col2:
                            st.image('G-P (11).jpeg')
                            st.metric(label='ORDER NO',value='11')
                      with col3:
                            st.image('G-P (12).jpeg')
                            st.metric(label='ORDER NO',value='12')         
                      st.divider()  
                      col1, col2,col3 = st.columns(3)
                      with col1:
                            st.image('G-P (16).jpeg')
                            st.metric(label='ORDER NO',value='16')
                      with col2:
                            st.image('G-P (17).jpeg')
                            st.metric(label='ORDER NO',value='17')
                      with col3:
                            st.image('G-P (18).jpeg')
                            st.metric(label='ORDER NO',value='18')         
                      st.divider()  

                           




                     
                          


                         

                            
                      
    
          
                

    
        






            

    












