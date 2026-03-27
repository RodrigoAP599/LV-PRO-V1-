# # import pandas as pd
# # import streamlit as st
# # import plotly.express as px

# # st.set_page_config(layout="wide")

# # st.title("🧺 Dashboard Lavandería")

# # # ==============================
# # # CARGA DE ARCHIVO
# # # ==============================
# # archivo = st.file_uploader("Sube tu Excel", type=["xlsx"])

# # if archivo:
# #     df = pd.read_excel(archivo)

# #     # LIMPIAR COLUMNAS
# #     df.columns = (
# #         df.columns
# #         .str.strip()
# #         .str.upper()
# #         .str.replace("Á", "A")
# #         .str.replace("É", "E")
# #         .str.replace("Í", "I")
# #         .str.replace("Ó", "O")
# #         .str.replace("Ú", "U")
# #     )

# #     # FECHAS
# #     if "FECHA INGRESO" in df.columns:
# #         df["FECHA INGRESO"] = pd.to_datetime(df["FECHA INGRESO"], errors="coerce")

# #     if "FECHA DE SALIDA" in df.columns:
# #         df["FECHA DE SALIDA"] = pd.to_datetime(df["FECHA DE SALIDA"], errors="coerce")

# #     if "LEAD TIME" not in df.columns:
# #         df["LEAD TIME"] = 1

# #     # ==============================
# #     # FILTROS
# #     # ==============================
# #     st.sidebar.header("Filtros")

# #     clientes = []
# #     if "CLIENTE" in df.columns:
# #         clientes = st.sidebar.multiselect("Cliente", df["CLIENTE"].dropna().unique())

# #     clasif = []
# #     if "CLASIFICACION L.TIME" in df.columns:
# #         clasif = st.sidebar.multiselect("Clasificación", df["CLASIFICACION L.TIME"].dropna().unique())

# #     if clientes:
# #         df = df[df["CLIENTE"].isin(clientes)]

# #     if clasif:
# #         df = df[df["CLASIFICACION L.TIME"].isin(clasif)]

# #     # ==============================
# #     # GRAFICOS
# #     # ==============================

# #     col1, col2 = st.columns(2)

# #     # BOX
# #     if {"CLIENTE", "LEAD TIME"}.issubset(df.columns):
# #         fig_box = px.box(df, x="CLIENTE", y="LEAD TIME", title="Lead Time por Cliente")
# #         col1.plotly_chart(fig_box, use_container_width=True)

# #     # GANTT
# #     if {"FECHA INGRESO", "FECHA DE SALIDA", "COCHE"}.issubset(df.columns):
# #         fig_gantt = px.timeline(
# #             df,
# #             x_start="FECHA INGRESO",
# #             x_end="FECHA DE SALIDA",
# #             y="COCHE"
# #         )
# #         fig_gantt.update_yaxes(autorange="reversed")
# #         col2.plotly_chart(fig_gantt, use_container_width=True)

# #     # FLUJO SIMPLE
# #     if "FECHA INGRESO" in df.columns:
# #         df["Y"] = range(len(df))
# #         fig_flujo = px.scatter(df, x="FECHA INGRESO", y="Y", color="CLIENTE")
# #         st.plotly_chart(fig_flujo, use_container_width=True)

# #     # TABLA
# #     st.dataframe(df)

# # else:
# #     st.info("Sube un archivo Excel para comenzar")

# import pandas as pd
# import plotly.graph_objects as go
# import numpy as np
# import time

# # =========================
# # DATA SIMULADA
# # =========================
# np.random.seed(1)

# df = pd.DataFrame({
#     "lote": range(1, 21),
#     "cliente": np.random.choice(["A", "B", "C"], 20),
#     "estado": np.random.choice(["entrada", "wip", "salida"], 20),
# })

# # =========================
# # POSICIONES
# # =========================
# posiciones = {
#     "entrada": 0,
#     "wip": 1,
#     "salida": 2
# }

# df["x"] = df["estado"].map(posiciones)
# df["y"] = np.random.rand(len(df))

# # =========================
# # ANIMACIÓN
# # =========================
# frames = []

# for step in range(5):
#     temp = df.copy()

#     # simular avance
#     temp["x"] = temp["x"] + np.random.choice([0, 0.2], len(temp))

#     frames.append(go.Frame(
#         data=[
#             go.Scatter(
#                 x=temp["x"],
#                 y=temp["y"],
#                 mode="markers",
#                 marker=dict(size=12)
#             )
#         ]
#     ))

# fig = go.Figure(
#     data=[
#         go.Scatter(
#             x=df["x"],
#             y=df["y"],
#             mode="markers",
#             marker=dict(size=12)
#         )
#     ],
#     layout=go.Layout(
#         title="Flujo: Entrada → WIP → Salida",
#         xaxis=dict(
#             tickvals=[0,1,2],
#             ticktext=["Entrada", "WIP", "Salida"]
#         ),
#         updatemenus=[dict(
#             type="buttons",
#             buttons=[dict(label="Play",
#                           method="animate",
#                           args=[None])]
#         )]
#     ),
#     frames=frames
# )

# fig.show()


# import plotly.express as px

# # =========================
# # DATA
# # =========================
# df_lt = pd.DataFrame({
#     "lote": range(1, 21),
#     "cliente": np.random.choice(["A", "B", "C"], 20),
#     "lead_time": np.random.uniform(1, 10, 20)
# })

# # =========================
# # FILTRO (simulado)
# # =========================
# lotes_seleccionados = [1,2,3,4,5,6,7]

# df_filtrado = df_lt[df_lt["lote"].isin(lotes_seleccionados)]

# # =========================
# # GRAFICO
# # =========================
# fig = px.bar(
#     df_filtrado,
#     x="cliente",
#     y="lead_time",
#     color="cliente",
#     title="Lead Time por Cliente (Filtrado por Lotes)"
# )

# fig.show()

# import plotly.express as px

# # =========================
# # DATA
# # =========================
# df_gantt = pd.DataFrame({
#     "cliente": ["A","A","B","B","C"],
#     "lote": ["L1","L2","L3","L4","L5"],
#     "inicio": pd.date_range("2024-01-01", periods=5),
#     "fin": pd.date_range("2024-01-03", periods=5)
# })

# # =========================
# # GANTT
# # =========================
# fig = px.timeline(
#     df_gantt,
#     x_start="inicio",
#     x_end="fin",
#     y="cliente",
#     color="cliente",
#     text="lote"
# )

# # mejorar visibilidad
# fig.update_traces(
#     textposition="inside",
#     marker_line_color='black',
#     marker_line_width=1.5
# )

# fig.update_layout(
#     title="Gantt por Cliente (Lotes)",
#     xaxis_title="Tiempo",
#     yaxis_title="Cliente"
# )

# fig.show()

#================2 interacion==========================#

# import pandas as pd
# import dash
# from dash import dcc, html, Input, Output, dash_table
# import plotly.express as px
# import base64
# import io

# # ======================================================
# # CONFIG
# # ======================================================
# FILE_PATH = "LEAD TIME LAVANDERIA ANALISIS.xlsx"

# # ======================================================
# # LIMPIEZA DE DATA
# # ======================================================
# def clean_data(df):

#     df.columns = df.columns.str.strip().str.upper()

#     # Renombrar variantes comunes
#     df.rename(columns={
#         "FECHA_INGRESO": "FECHA INGRESO",
#         "FECHA_SALIDA": "FECHA DE SALIDA",
#         "CLASIFICACION": "CLASIFICACION L.TIME",
#     }, inplace=True)

#     # Crear columnas si no existen
#     for col in ["CLIENTE", "COCHE", "LOTE", "CLASIFICACION L.TIME"]:
#         if col not in df.columns:
#             df[col] = "SIN DATO"

#     # Fechas
#     df["FECHA INGRESO"] = pd.to_datetime(df.get("FECHA INGRESO"), errors="coerce")
#     df["FECHA DE SALIDA"] = pd.to_datetime(df.get("FECHA DE SALIDA"), errors="coerce")

#     # Lead Time
#     if "LEAD TIME" not in df.columns:
#         df["LEAD TIME"] = (df["FECHA DE SALIDA"] - df["FECHA INGRESO"]).dt.days

#     df["LEAD TIME"] = df["LEAD TIME"].fillna(1)

#     # Filtro Lavandería #2 (robusto)
#     if "LAVANDERIA" in df.columns:
#         df["LAVANDERIA"] = df["LAVANDERIA"].astype(str).str.strip().str.upper()
#         df = df[df["LAVANDERIA"].isin(["2", "LAVANDERIA 2", "L2"])]

#     print("Columnas:", df.columns)
#     print("Filas:", len(df))

#     return df


# # ======================================================
# # CARGA INICIAL
# # ======================================================
# def load_data(path):
#     try:
#         df = pd.read_excel(path)
#         return clean_data(df)
#     except Exception as e:
#         print("Error cargando archivo:", e)
#         return pd.DataFrame()

# df_global = load_data(FILE_PATH)

# # ======================================================
# # APP
# # ======================================================
# app = dash.Dash(__name__)
# server = app.server

# app.layout = html.Div([

#     dcc.Store(id="store-data", data=df_global.to_dict("records")),

#     # SIDEBAR
#     html.Div([
#         html.H3("Filtros"),

#         dcc.Dropdown(id="cliente", multi=True, placeholder="Cliente"),
#         dcc.Dropdown(id="clasificacion", multi=True,
#                      options=[
#                          {"label": "NORMAL", "value": "NORMAL"},
#                          {"label": "ALTO", "value": "ALTO"},
#                          {"label": "CRITICO", "value": "CRITICO"},
#                      ]),
#         dcc.Dropdown(id="lote", multi=True, placeholder="Lote"),

#         dcc.DatePickerRange(id="fecha"),

#         html.Br(),
#         dcc.Upload(
#             id="upload-data",
#             children=html.Button("Subir Excel")
#         ),

#         html.Button("Limpiar datos", id="clear-data"),

#     ], style={"width": "20%", "display": "inline-block", "verticalAlign": "top"}),

#     # MAIN
#     html.Div([

#         html.H2("🧺 Flujo Animado - Lavandería #2"),
#         dcc.Graph(id="flujo"),

#         html.H2("DISTRIBUCIÓN DE LEAD TIME POR CLIENTE"),
#         dcc.Graph(id="boxplot"),

#         html.H2("GANTT DE INGRESO Y SALIDA POR COCHE"),
#         dcc.Graph(id="gantt"),

#         html.H2("DETALLE DE DATOS"),
#         dash_table.DataTable(id="tabla", page_size=10)

#     ], style={"width": "75%", "display": "inline-block", "marginLeft": "20px"})
# ])

# # ======================================================
# # UPLOAD + RESET
# # ======================================================
# @app.callback(
#     Output("store-data", "data"),
#     Input("upload-data", "contents"),
#     Input("clear-data", "n_clicks"),
#     prevent_initial_call=True
# )
# def update_store(contents, clear):

#     ctx = dash.callback_context

#     if not ctx.triggered:
#         return dash.no_update

#     trigger = ctx.triggered[0]["prop_id"].split(".")[0]

#     if trigger == "clear-data":
#         return df_global.to_dict("records")

#     if contents:
#         content_type, content_string = contents.split(",")
#         decoded = base64.b64decode(content_string)
#         df = pd.read_excel(io.BytesIO(decoded))

#         df = clean_data(df)

#         return df.to_dict("records")

#     return dash.no_update


# # ======================================================
# # CALLBACK PRINCIPAL
# # ======================================================
# @app.callback(
#     Output("cliente", "options"),
#     Output("lote", "options"),
#     Output("flujo", "figure"),
#     Output("boxplot", "figure"),
#     Output("gantt", "figure"),
#     Output("tabla", "data"),

#     Input("store-data", "data"),
#     Input("cliente", "value"),
#     Input("clasificacion", "value"),
#     Input("lote", "value"),
#     Input("fecha", "start_date"),
#     Input("fecha", "end_date"),
# )
# def update(data, clientes, clasif, lotes, start, end):

#     df = pd.DataFrame(data)

#     if df.empty:
#         return [], [], {}, {}, {}, []

#     # FILTROS
#     if clientes:
#         df = df[df["CLIENTE"].isin(clientes)]

#     if clasif:
#         df = df[df["CLASIFICACION L.TIME"].isin(clasif)]

#     if lotes:
#         df = df[df["LOTE"].isin(lotes)]

#     if start:
#         df = df[df["FECHA INGRESO"] >= pd.to_datetime(start)]

#     if end:
#         df = df[df["FECHA INGRESO"] <= pd.to_datetime(end)]

#     # DROPDOWNS
#     clientes_opt = [{"label": str(c), "value": str(c)} for c in df["CLIENTE"].dropna().unique()]
#     lotes_opt = [{"label": str(l), "value": str(l)} for l in df["LOTE"].dropna().unique()]

#     # FLUJO
#     df_flujo = df.dropna(subset=["FECHA INGRESO", "FECHA DE SALIDA"])

#     if df_flujo.empty:
#         fig_flujo = {}
#     else:
#         frames = []
#         fechas = pd.date_range(df_flujo["FECHA INGRESO"].min(), df_flujo["FECHA DE SALIDA"].max())

#         for fecha in fechas:
#             temp = df_flujo.copy()

#             temp["X"] = 0
#             temp.loc[temp["FECHA INGRESO"] <= fecha, "X"] = 1
#             temp.loc[temp["FECHA DE SALIDA"] <= fecha, "X"] = 2

#             temp["Y"] = range(len(temp))
#             temp["FRAME"] = fecha

#             frames.append(temp)

#         sim_df = pd.concat(frames)

#         fig_flujo = px.scatter(
#             sim_df,
#             x="X",
#             y="Y",
#             animation_frame=sim_df["FRAME"].astype(str),
#             color="CLASIFICACION L.TIME",
#             size="LEAD TIME",
#             hover_data=["COCHE", "CLIENTE"]
#         )

#         fig_flujo.update_layout(
#             xaxis=dict(tickvals=[0,1,2], ticktext=["Entrada", "WIP", "Salida"]),
#             yaxis=dict(showticklabels=False)
#         )

#     # BOXPLOT
#     fig_box = px.box(df, x="CLIENTE", y="LEAD TIME")

#     # GANTT
#     fig_gantt = px.timeline(df, x_start="FECHA INGRESO", x_end="FECHA DE SALIDA", y="COCHE")
#     fig_gantt.update_yaxes(autorange="reversed")

#     return clientes_opt, lotes_opt, fig_flujo, fig_box, fig_gantt, df.to_dict("records")


# # ======================================================
# # RUN
# # ======================================================
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=10000)

#==============3 iteracion===========================================#
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # ======================================================
# # CONFIG
# # ======================================================
# st.set_page_config(layout="wide")
# st.title("🧺 LAVANDERÍA #2 - ANÁLISIS DE LEAD TIME")

# # ======================================================
# # FUNCION DE CARGA
# # ======================================================
# def load_data(file):
#     try:
#         df = pd.read_excel(file)

#         # Normalizar columnas
#         df.columns = df.columns.str.strip().str.upper()

#         # Validar columnas mínimas
#         required = ["CLIENTE", "COCHE", "FECHA INGRESO", "FECHA DE SALIDA"]
#         for col in required:
#             if col not in df.columns:
#                 st.error(f"Falta la columna: {col}")
#                 return pd.DataFrame()

#         # Fechas
#         df["FECHA INGRESO"] = pd.to_datetime(df["FECHA INGRESO"], errors="coerce")
#         df["FECHA DE SALIDA"] = pd.to_datetime(df["FECHA DE SALIDA"], errors="coerce")

#         # Lead Time
#         if "LEAD TIME" not in df.columns:
#             df["LEAD TIME"] = (
#                 (df["FECHA DE SALIDA"] - df["FECHA INGRESO"]).dt.days
#             )

#         # Clasificación
#         if "CLASIFICACION L.TIME" not in df.columns:
#             df["CLASIFICACION L.TIME"] = "NORMAL"

#         return df

#     except Exception as e:
#         st.error(f"Error cargando archivo: {e}")
#         return pd.DataFrame()


# # ======================================================
# # SIDEBAR
# # ======================================================
# st.sidebar.header("Filtros")

# archivo = st.sidebar.file_uploader("Subir Excel", type=["xlsx"])

# df = pd.DataFrame()

# if archivo:
#     df = load_data(archivo)

# if df.empty:
#     st.warning("Sube un archivo para comenzar")
#     st.stop()

# # ======================================================
# # FILTROS
# # ======================================================
# clientes = st.sidebar.multiselect(
#     "Cliente",
#     options=df["CLIENTE"].dropna().unique(),
#     key="cliente_filtro"
# )

# clasificacion = st.sidebar.multiselect(
#     "Clasificación",
#     options=df["CLASIFICACION L.TIME"].dropna().unique(),
#     key="clasif_filtro"
# )

# fecha_rango = st.sidebar.date_input(
#     "Rango de fechas",
#     key="fecha_filtro"
# )

# df_f = df.copy()

# # Aplicar filtros
# if clientes:
#     df_f = df_f[df_f["CLIENTE"].isin(clientes)]

# if clasificacion:
#     df_f = df_f[df_f["CLASIFICACION L.TIME"].isin(clasificacion)]

# if isinstance(fecha_rango, tuple) and len(fecha_rango) == 2:
#     inicio, fin = fecha_rango
#     df_f = df_f[
#         (df_f["FECHA INGRESO"] >= pd.to_datetime(inicio)) &
#         (df_f["FECHA INGRESO"] <= pd.to_datetime(fin))
#     ]

# # ======================================================
# # KPIs
# # ======================================================
# col1, col2, col3 = st.columns(3)

# col1.metric("Total Registros", len(df_f))
# col2.metric("Lead Time Promedio", round(df_f["LEAD TIME"].mean(), 2))
# col3.metric("Clientes", df_f["CLIENTE"].nunique())

# # ======================================================
# # FLUJO ANIMADO
# # ======================================================
# st.subheader("🔄 Flujo (Entrada → WIP → Salida)")

# df_flujo = df_f.dropna(subset=["FECHA INGRESO", "FECHA DE SALIDA"])

# if not df_flujo.empty:

#     frames = []
#     fechas = pd.date_range(
#         df_flujo["FECHA INGRESO"].min(),
#         df_flujo["FECHA DE SALIDA"].max(),
#         freq="D"
#     )

#     for fecha in fechas:
#         temp = df_flujo.copy()

#         temp["X"] = 0
#         temp.loc[temp["FECHA INGRESO"] <= fecha, "X"] = 1
#         temp.loc[temp["FECHA DE SALIDA"] <= fecha, "X"] = 2

#         temp["ESTADO"] = temp["X"].map({
#             0: "Entrada",
#             1: "WIP",
#             2: "Salida"
#         })

#         temp["Y"] = range(len(temp))
#         temp["FRAME"] = fecha

#         frames.append(temp)

#     sim_df = pd.concat(frames)
#     sim_df["FRAME_STR"] = sim_df["FRAME"].astype(str)

#     fig_flujo = px.scatter(
#         sim_df,
#         x="X",
#         y="Y",
#         animation_frame="FRAME_STR",
#         color="CLASIFICACION L.TIME",
#         size="LEAD TIME",
#         hover_data=["COCHE", "CLIENTE"]
#     )

#     fig_flujo.update_layout(
#         xaxis=dict(
#             tickvals=[0, 1, 2],
#             ticktext=["Entrada", "WIP", "Salida"]
#         ),
#         yaxis=dict(showticklabels=False)
#     )

#     st.plotly_chart(fig_flujo, use_container_width=True)

# else:
#     st.info("No hay datos para flujo")

# # ======================================================
# # BOXPLOT
# # ======================================================
# st.subheader("📊 Lead Time por Cliente")

# fig_box = px.box(
#     df_f,
#     x="CLIENTE",
#     y="LEAD TIME",
#     color="CLASIFICACION L.TIME"
# )

# st.plotly_chart(fig_box, use_container_width=True)

# # ======================================================
# # GANTT
# # ======================================================
# st.subheader("📅 Gantt de Procesos")

# df_gantt = df_f.dropna(subset=["FECHA INGRESO", "FECHA DE SALIDA"])

# if not df_gantt.empty:
#     fig_gantt = px.timeline(
#         df_gantt,
#         x_start="FECHA INGRESO",
#         x_end="FECHA DE SALIDA",
#         y="COCHE",
#         color="CLASIFICACION L.TIME"
#     )

#     fig_gantt.update_yaxes(autorange="reversed")

#     st.plotly_chart(fig_gantt, use_container_width=True)

# else:
#     st.info("No hay datos para Gantt")

# # ======================================================
# # TABLA
# # ======================================================
# st.subheader("📋 Datos")

# st.dataframe(df_f, use_container_width=True)

#================4 intento===============================#

import streamlit as st
import pandas as pd
import plotly.express as px

# ======================================================
# CONFIG
# ======================================================
st.set_page_config(layout="wide")
st.title("🧺 LAVANDERÍA #2 - ANÁLISIS DE LEAD TIME")

# ======================================================
# FUNCION DE CARGA
# ======================================================
def load_data(file):
    try:
        df = pd.read_excel(file)
        df.columns = df.columns.str.strip().str.upper()
        # Columnas mínimas
        required = ["CLIENTE", "COCHE", "FECHA INGRESO", "FECHA DE SALIDA"]
        for col in required:
            if col not in df.columns:
                st.error(f"Falta la columna: {col}")
                return pd.DataFrame()
        # Fechas
        df["FECHA INGRESO"] = pd.to_datetime(df["FECHA INGRESO"], errors="coerce")
        df["FECHA DE SALIDA"] = pd.to_datetime(df["FECHA DE SALIDA"], errors="coerce")
        # Lead Time
        if "LEAD TIME" not in df.columns:
            df["LEAD TIME"] = (df["FECHA DE SALIDA"] - df["FECHA INGRESO"]).dt.days
        # Clasificación Lead Time
        if "CLASIFICACION L.TIME" not in df.columns:
            df["CLASIFICACION L.TIME"] = "NORMAL"
        # Clasificación por lote
        if "LT" not in df.columns:
            df["LT"] = "SIN CLASIFICAR"
        df["LT"] = df["LT"].fillna("SIN CLASIFICAR")
        return df
    except Exception as e:
        st.error(f"Error cargando archivo: {e}")
        return pd.DataFrame()

# ======================================================
# SIDEBAR - SUBIR ARCHIVO Y FILTROS
# ======================================================
st.sidebar.header("Filtros")
archivo = st.sidebar.file_uploader("Subir Excel", type=["xlsx"])
df = pd.DataFrame()
if archivo:
    df = load_data(archivo)
else:
    st.info("Sube un archivo para comenzar")
    st.stop()

# ==========================
# FILTROS
# ==========================
# Cliente
clientes_sel = st.sidebar.multiselect(
    "Cliente",
    options=df["CLIENTE"].dropna().unique()
)

# Clasificación L.Time
clasif_sel = st.sidebar.multiselect(
    "Clasificación L.Time",
    options=df["CLASIFICACION L.TIME"].dropna().unique()
)

# Clasificación por Lote (LT) - considerar vacíos
lt_sel = st.sidebar.multiselect(
    "Clasificación por Lote (LT)",
    options=df["LT"].unique()
)

# Fechas
min_fecha = df["FECHA INGRESO"].min()
max_fecha = df["FECHA INGRESO"].max()
fecha_rango = st.sidebar.date_input(
    "Rango de fechas",
    value=(min_fecha, max_fecha)
)

# ==========================
# APLICAR FILTROS
# ==========================
df_f = df.copy()
if clientes_sel:
    df_f = df_f[df_f["CLIENTE"].isin(clientes_sel)]
if clasif_sel:
    df_f = df_f[df_f["CLASIFICACION L.TIME"].isin(clasif_sel)]
if lt_sel:
    df_f = df_f[df_f["LT"].isin(lt_sel)]
# Filtro de fechas
if isinstance(fecha_rango, tuple) and len(fecha_rango) == 2:
    inicio, fin = fecha_rango
    df_f = df_f[
        (df_f["FECHA INGRESO"] >= pd.to_datetime(inicio)) &
        (df_f["FECHA INGRESO"] <= pd.to_datetime(fin))
    ]

# ======================================================
# KPIs
# ======================================================
col1, col2, col3 = st.columns(3)
col1.metric("Total Registros", len(df_f))
col2.metric("Lead Time Promedio", round(df_f["LEAD TIME"].mean(), 2))
col3.metric("Clientes", df_f["CLIENTE"].nunique())

# ======================================================
# FLUJO ANIMADO
# ======================================================
st.subheader("🔄 Flujo Operacional (Coches, Lotes y Clientes)")
df_flujo = df_f.dropna(subset=["FECHA INGRESO", "FECHA DE SALIDA"])
if not df_flujo.empty:
    frames = []
    fechas = pd.date_range(df_flujo["FECHA INGRESO"].min(), df_flujo["FECHA DE SALIDA"].max(), freq="D")
    for fecha in fechas:
        temp = df_flujo.copy()
        # Estado: Entrada=0, WIP=1, Salida=2
        temp["X"] = 0
        temp.loc[temp["FECHA INGRESO"] <= fecha, "X"] = 1
        temp.loc[temp["FECHA DE SALIDA"] <= fecha, "X"] = 2
        temp["ESTADO"] = temp["X"].map({0:"Entrada",1:"WIP",2:"Salida"})
        temp["FRAME"] = fecha
        frames.append(temp)
    sim_df = pd.concat(frames)
    sim_df["FRAME_STR"] = sim_df["FRAME"].astype(str)

    fig_flujo = px.scatter(
        sim_df,
        x="X",
        y="COCHE",
        animation_frame="FRAME_STR",
        color="LT",
        size="LEAD TIME",
        text="LT",
        hover_data={"CLIENTE":True,"LT":True,"COCHE":True,"FECHA INGRESO":True,"FECHA DE SALIDA":True,"ESTADO":True},
    )
    fig_flujo.update_traces(textposition="top center", marker=dict(opacity=0.8))
    fig_flujo.update_layout(
        xaxis=dict(
            tickvals=[0,1,2],
            ticktext=["Entrada","WIP","Salida"],
            title="Estado del Proceso"
        ),
        yaxis_title="Coche",
        legend_title="Lote (LT)",
        height=600
    )
    st.plotly_chart(fig_flujo, use_container_width=True)

    # Tabla Cliente → Lotes
    st.subheader("📦 Relación Cliente → Lotes")
    relacion = df_flujo.groupby("CLIENTE")["LT"].apply(lambda x: ', '.join(map(str, x.unique()))).reset_index()
    st.dataframe(relacion, use_container_width=True)

else:
    st.info("No hay datos para flujo")

# ======================================================
# BOX PLOT
# ======================================================
st.subheader("📊 Lead Time por Cliente")
if not df_f.empty:
    fig_box = px.box(df_f, x="CLIENTE", y="LEAD TIME", color="LT")
    st.plotly_chart(fig_box, use_container_width=True)
else:
    st.info("No hay datos para el boxplot")

# ======================================================
# GANTT
# ======================================================
st.subheader("📅 Gantt de Procesos")
if not df_flujo.empty:
    fig_gantt = px.timeline(
        df_flujo,
        x_start="FECHA INGRESO",
        x_end="FECHA DE SALIDA",
        y="COCHE",
        color="LT"
    )
    fig_gantt.update_yaxes(autorange="reversed")
    st.plotly_chart(fig_gantt, use_container_width=True)
else:
    st.info("No hay datos para Gantt")

# ======================================================
# TABLA COMPLETA
# ======================================================
st.subheader("📋 Datos")
st.dataframe(df_f, use_container_width=True)