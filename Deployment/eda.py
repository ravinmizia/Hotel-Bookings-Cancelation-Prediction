import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image


#melebarkan
st.set_page_config(
    page_title='Customer Booking Pattern',
    layout='wide',
    initial_sidebar_state='expanded'

)

st.markdown("""<style>.reportview-container {background: "5160549.jpg"}.sidebar .sidebar-content {background: "5160549.jpg"}</style>""",unsafe_allow_html=True)



def run():

    # Set title
    st.markdown("<h1 style='text-align: center; color: white;'>Customer Booking Canceled? </h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: grey ;'>Silahkan melihat-lihat !</h3>", unsafe_allow_html=True)



    # library pillow buat gambar
    image = Image.open('grandbUdapest.jpg')
    st.markdown('---')
    st.image(image, caption=' "WELLCOME TO GRAND BUDAPEST HOTEL !" ') 

    # descripsi
    st.write('### Halaman ini berisi Eksplorasi Data Customer ')

    # Membuat Garis lurus
    st.markdown('---')


    # Nampilin dataframe
    st.write('### Reservation Details')

    data = pd.read_csv('Hotel Reservations.csv')
    st.dataframe(data.head(5))

    st.markdown('***')
    #barplot
    fig = plt.figure(figsize=(8,5))

    ###########################################
    st.write('### Trend Bulan Cancelation')
    #plot death chance
    # probability death event
    # bulan apa saja mereka biasanya cancel ?
    fig, (ax1, ax2) = plt.subplots(1, 2,  figsize=(15, 5))
    sns.histplot(data = data[data.booking_status == 'Canceled'],x='arrival_month', hue='arrival_year', palette=sns.color_palette('dark',9), ax=ax1)
    ax1.set_title('plot CANCELATION')
    #ax1.set_ylim(2000)
    sns.histplot(data = data[data.booking_status == 'Not_Canceled'],x='arrival_month', hue='arrival_year', palette=sns.color_palette('dark',9), ax=ax2)
    ax2.set_title('plot NON CANCELATION')
    #ax2.set_ylim(2000)
    st.pyplot(fig)
    st.markdown('***')


    ####################################################
    fig3, (ax1, ax2) = plt.subplots(1, 2,  figsize=(20, 5))
    st.write('### Metode Booking dan Special Request')
    # presentase cancel online dan offline
    sns.histplot(data = data,x='market_segment_type', hue='booking_status', ax=ax1)
    #jumlah data cancel

    sns.histplot(data = data,x='no_of_special_requests', hue='booking_status',binwidth=0.8, ax=ax2)
    ax2.axhline(data[(data.booking_status == 'Not_Canceled') & (data.no_of_special_requests == 1)].no_of_special_requests.count(),ls='--')
    ax2.axhline(data[(data.booking_status == 'Canceled') & (data.no_of_special_requests == 1)].no_of_special_requests.count(),ls='--',c='orange')
    st.pyplot(fig3)
    st.markdown('***')



    ###############################################
    st.write('### Room Booked Analysis')
    fig3, (ax1, ax2) = plt.subplots(1, 2,  figsize=(20, 5))
    sns.histplot(data[data.booking_status=='Canceled'], x='avg_price_per_room', hue='room_type_reserved', fill=True, ax=ax1, kde=True)
    ax1.set_title('Canceled Room')
    ax1.set_xlim(0,250)
    ax1.set_ylim(0,1300)
    ax1.axvline(data[data.booking_status == 'Canceled'].avg_price_per_room.mean(),ls='--', c='r')

    sns.histplot(data[data.booking_status=='Not_Canceled'], x='avg_price_per_room', hue='room_type_reserved', fill=True, ax=ax2, kde=True)
    ax2.set_title('Not_Canceled Room')
    ax2.set_xlim(0,250)
    ax2.set_ylim(0,1300)
    ax2.axvline(data[data.booking_status == 'Not_Canceled'].avg_price_per_room.mean(),ls='--', c='r')
    st.pyplot(fig3)
    st.markdown('***')


    ####################################################
    st.write('### Lead Time & Booking Status')
    fig4 = sns.displot(data, x='lead_time', hue='booking_status', kind='kde', fill=True, height=5, aspect=1.5)
    plt.axvline(data[data.booking_status == 'Not_Canceled'].lead_time.mean(),ls='--')
    plt.axvline(data[data.booking_status == 'Canceled'].lead_time.mean(),ls='--', c='orange')
    st.pyplot(fig4)

    st.markdown('***')



    #hist berdasarkan intpput user
    st.write('### Histogram Imputed Users')
    pilihan = st.selectbox('Pilih Kolum : ', ('lead_time', 'avg_price_per_room', 'no_of_special_requests', 'repeated_guest'))
    fig=plt.figure(figsize=(15,5))
    sns.histplot(data[pilihan], bins=  30, kde=True)
    st.pyplot(fig)


    st.markdown('***')



if __name__ == '__main__':
    run()