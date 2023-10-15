import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as io

st.title(" NH 투자증권 빅데이터 경진대회 CHART - by 차가운 자본주의" )

chart_df = pd.read_csv("full_table.csv")
chart_df = chart_df.set_index("Date")
chart_df.index = pd.to_datetime(chart_df.index)
is_percent = 100

st.subheader("일별, 장 시작 30분 수익률 비교")
title_name = 'KOSPI'


st.text("KOSPI (코스피지수 : KOSPI Index")
main_fig = go.Figure(
    data = [
        go.Bar(
            x = chart_df.index,
            y = chart_df['KOSPI_d_rtn']* is_percent,
            name= title_name + " 일별 수익률",
            offsetgroup = 0
            ),

        go.Bar(
            x = chart_df.index,
            y = chart_df['KOSPI_Index_30_rtn']* is_percent,
            name= title_name + " 장 시작 30분 수익률",
            offsetgroup = 0
            ),

        ]
)

main_fig.update_layout(title=title_name, xaxis_title='기간', yaxis_title='수익률 (%)')
st.plotly_chart(main_fig, use_container_width=True)


st.text("KOSPI LARGE CAP (유가증권시장 대형주 지수 : KOSPLMKC Index)")
title_name2 = "유가증권시장 대형주 지수"

main_fig2 = go.Figure(
    data = [
        go.Bar(
            x = chart_df.index,
            y = chart_df['KOSPLMKC_d_rtn']* is_percent,
            name= title_name2 + " 일별 수익률",
            offsetgroup = 0
            ),

        go.Bar(
            x = chart_df.index,
            y = chart_df['KOSPLMKC_Index_30_rtn']* is_percent,
            name=title_name2 +" 장 시작 30분 수익률",
            offsetgroup = 0
            ),

        ]
)

main_fig2.update_layout(title=title_name2, xaxis_title='기간', yaxis_title='수익률 (%)')
st.plotly_chart(main_fig2, use_container_width=True)



st.text("KOSPI MIDDLE CAP (유가증권시장 중형주 지수 : KOSPMMKC Index)")
title_name3 =  "유가증권시장 중형주 지수"
main_fig3 = go.Figure(
    data = [
        go.Bar(
            x = chart_df.index,
            y = chart_df['KOSPMMKC_d_rtn']* is_percent,
            name= title_name3 + " 일별 수익률",
            offsetgroup = 0
            ),

        go.Bar(
            x = chart_df.index,
            y = chart_df['KOSPMMKC_Index_30_rtn']* is_percent,
            name=title_name3 +" 장 시작 30분 수익률",
            offsetgroup = 0
            ),

        ]
)

main_fig3.update_layout(title=title_name3, xaxis_title='기간', yaxis_title='수익률 (%)')
st.plotly_chart(main_fig3, use_container_width=True)


st.text("KOSPI SMALL CAP (유가증권시장 소형주 지수 : KOSPSMKC Index)")
title_name4 = "유가증권시장 소형주 지수"

main_fig4 = go.Figure(
    data = [
        go.Bar(
            x = chart_df.index,
            y = chart_df['KOSPSMKC_d_rtn']* is_percent,
            name= title_name4 + " 일별 수익률",
            offsetgroup = 0
            ),

        go.Bar(
            x = chart_df.index,
            y = chart_df['KOSPSMKC_Index_30_rtn']* is_percent,
            name=title_name4 +" 장 시작 30분 수익률",
            offsetgroup = 0
            ),

        ]
)


main_fig4.update_layout(title=title_name4, xaxis_title='기간', yaxis_title='수익률 (%)')
st.plotly_chart(main_fig4, use_container_width=True)




st.text("KOSDAQ (코스닥지수 : KOSDAQ Index)")
title_name5 = "코스닥 지수"

main_fig5 = go.Figure(
    data = [
        go.Bar(
            x = chart_df.index,
            y = chart_df['KOSDAQ_d_rtn']* is_percent,
            name= title_name5 + " 일별 수익률",
            offsetgroup = 0
            ),

        go.Bar(
            x = chart_df.index,
            y = chart_df['KOSDAQ_Index_30_rtn']* is_percent,
            name=title_name5 +" 장 시작 30분 수익률",
            offsetgroup = 0
            ),

        ]
)


main_fig5.update_layout(title=title_name5, xaxis_title='기간', yaxis_title='수익률 (%)')
st.plotly_chart(main_fig5, use_container_width=True)



st.subheader("NASDAQ 소형 중형 대형 비교")
na_drop = True
if na_drop:
    chart_droped_na_df = chart_df[['lrg_cap_rtn', 'mid_cap_rtn', 'sml_cap_rtn',
                                  'spread_lrg', 'spread_mid', 'spread_sml',
                                  'lrg_buy_rate', 'mid_buy_rate', 'sml_buy_rate']].dropna()
else:
    chart_droped_na_df = chart_df



st.text("수익률 비교")

sub_fig = make_subplots(specs=[[{"secondary_y": True}]])
sub_fig.add_trace(

    go.Scatter(
        x = chart_droped_na_df.index,
        y =  chart_droped_na_df["lrg_cap_rtn"].cumsum()*is_percent,
        name = "Large Cap"
        ),
    )

sub_fig.add_trace(
    go.Scatter(
        x = chart_droped_na_df.index,
        y = chart_droped_na_df["mid_cap_rtn"].cumsum()*is_percent,
        name = "Mid Cap"
        ),
    secondary_y=False
    )

sub_fig.add_trace(
    go.Scatter(
        x = chart_droped_na_df.index,
        y = chart_droped_na_df["sml_cap_rtn"].cumsum()*is_percent,
        name = "Small Cap"
        ),
    secondary_y=False
    )


sub_fig.update_layout(title='Nasdaq Market Cap Return Rate', xaxis_title='기간', yaxis_title=' 수익률 (%) ')
st.plotly_chart(sub_fig, use_container_width=True)


st.text("buy Volume")
sub_fig2 = make_subplots(specs=[[{"secondary_y": True}]])
sub_fig2.add_trace(

    go.Scatter(
        x = chart_droped_na_df.index,
        y =  chart_droped_na_df["lrg_buy_rate"],
        name = "Large Cap"
        ),
    )

sub_fig2.add_trace(
    go.Scatter(
        x = chart_droped_na_df.index,
        y = chart_droped_na_df["mid_buy_rate"],
        name = "Mid Cap"
        ),
    secondary_y=False
    )

sub_fig2.add_trace(
    go.Scatter(
        x = chart_droped_na_df.index,
        y = chart_droped_na_df["sml_buy_rate"],
        name = "Small Cap"
        ),
    secondary_y=False
    )


sub_fig2.update_layout(title='Nasdaq Market Cap Buy Volume', xaxis_title='기간', yaxis_title='비중 (%)')
st.plotly_chart(sub_fig2, use_container_width=True)


st.text("Corwin Schultz Spread")
sub_fig3 = make_subplots(specs=[[{"secondary_y": True}]])
sub_fig3.add_trace(

    go.Scatter(
        x = chart_droped_na_df.index,
        y =  chart_droped_na_df["spread_lrg"] * is_percent,
        name = "Large Cap"
        ),
    )

sub_fig3.add_trace(
    go.Scatter(
        x = chart_droped_na_df.index,
        y = chart_droped_na_df["spread_mid"]* is_percent,
        name = "Mid Cap"
        ),
    secondary_y=False
    )

sub_fig3.add_trace(
    go.Scatter(
        x = chart_droped_na_df.index,
        y = chart_droped_na_df["spread_sml"]* is_percent,
        name = "Small Cap"
        ),
    secondary_y=False
    )


sub_fig3.update_layout(title='Nasdaq Market Cap Corwin-Schultz Spread', xaxis_title='기간', yaxis_title='high-low spread')
st.plotly_chart(sub_fig3, use_container_width=True)