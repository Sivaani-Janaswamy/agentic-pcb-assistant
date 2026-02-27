import streamlit as st
import pandas as pd
from agents import generate_design   # Person A's function

st.set_page_config(page_title="Agentic AI PCB Assistant")

st.title("🤖 Agentic AI PCB Assistant")
st.write("Design your PCB using intelligent multi-agent reasoning.")

user_input = st.text_area(
    "Enter your circuit requirement:",
    placeholder="Example: Design a 5V 2A regulated power supply"
)

generate_button = st.button("Generate PCB Design")

if generate_button and user_input:

    with st.spinner("AI Agents are designing your PCB..."):

        result = generate_design(user_input)

        st.success("Design Generated Successfully!")
        st.divider()

        # ---------------------------
        # 🧠 Requirements
        # ---------------------------
        st.subheader("🧠 Requirement Analysis")

        req = result["requirements"]

        st.info(
            f"Output Voltage: {req['output_voltage']} V\n\n"
            f"Output Current: {req['output_current']} A\n\n"
            f"Circuit Type: {req['circuit_type']}"
        )

        # ---------------------------
        # 📦 Selected Components
        # ---------------------------
        st.subheader("📦 Selected Components")

        components = result["selected_components"]

        # Regulator
        regulator = components["regulator"]
        if regulator:
            st.write(f"**Regulator:** {regulator['name']} ({regulator['package']})")
            st.write(f"- Max Current: {regulator['max_current']} A")

        # Capacitors
        capacitors = components["capacitors"]
        if capacitors:
            st.write("**Capacitors:**")
            for cap in capacitors:
                st.write(f"- {cap['name']} ({cap['value']}, {cap['voltage_rating']}V)")

        # Diode
        diode = components["diode"]
        if diode:
            st.write(f"**Diode:** {diode['name']} (Max {diode['max_current']}A)")

        # ---------------------------
        # ⚠️ Validation
        # ---------------------------
        st.subheader("⚠️ Validation Report")

        validation = result["validation"]

        if validation["status"] == "PASS":
            st.success("Design Validation: PASS")
        elif validation["status"] == "WARNING":
            st.warning("Design Validation: WARNING")

        for issue in validation["issues"]:
            st.write(f"- {issue}")

        # ---------------------------
        # 🧭 Layout Recommendations
        # ---------------------------
        st.subheader("🧭 Layout Recommendations")

        for tip in result["layout_recommendations"]:
            st.write(f"- {tip}")

        # ---------------------------
        # 📋 BOM
        # ---------------------------
        st.subheader("📋 Bill of Materials (BOM)")

        bom_list = result["bom"]

        if bom_list:
            df = pd.DataFrame(bom_list)
            st.table(df)

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="Download BOM as CSV",
                data=csv,
                file_name="pcb_bom.csv",
                mime="text/csv"
            )