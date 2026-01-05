<h1 align="center"> Wireless-Modular Keyboard </h1>
<div align="center">
  <img width="80%" alt="image" src="https://github.com/user-attachments/assets/3de422af-304e-4d5e-8017-280363eabc6f" />
</div>
<p align="center">This project is a custom modular keyboard that has both wireless and wired capabilities. It also uses low profile, kailh choc hotswap switches increasing customizability and its overall asthetic. Additionally, it offers magnetic connection following the I2C protocol which ensures any type of module can connect to the main board effectively and securely.</p>
<h2></h2>
<h2> Features </h2>

- Works over USB-C (wired) or Bluetooth (wireless)
- Integrated magnetic pogo pins for stable I2C connection and adding external modules (numberpads, macropads or OLED modules)
- Integrated charging circuit for portability and wireless operation
- Uses Kailh Low Profile Choc hotswap sockets for key switch connections
- Features SK6805 addressable LEDs for customizable per key RGB lighting
- Includes a dedicated SWD interface for debugging and development
- A dedicated slide switch to manage battery life

<h2>Design - Main Board</h2>
<h3>Schematic</h3>
<img width="100%" alt="Schematic" src="https://github.com/user-attachments/assets/09c143b7-9dc0-413d-9ba6-27eaed69ed17" />
<h3>PCB</h3>
<img width="100%" alt="Back PCB" src="https://github.com/user-attachments/assets/c9973b4c-b40a-4385-b5e5-83c4a9ff7df9" />
<h4 align="center">PCB back</h4>
<img width="100%" alt="Front PCB" src="https://github.com/user-attachments/assets/23952d2b-95fd-44f1-86ce-78083ecc20eb" />
<h4 align="center">PCB front</h4>
<img width="100%" alt="PCB" src="https://github.com/user-attachments/assets/8b9dbc9f-bcd7-4657-84fe-700344f8f072" />
<h4 align="center">PCB</h4>
<img width="100%" alt="No-Components 3D View" src="https://github.com/user-attachments/assets/c00d64b3-ea89-4ade-b66a-ea81fc4e337f" />
<h4 align="center">PCB 3D model</h4>
<img width="100%" alt="3D view" src="https://github.com/user-attachments/assets/8fd15b56-dfcd-42e9-b987-81b10737f17e"/>
<h4 align="center">PCB 3D model with components</h4>
<h2>Design - Main Board</h2>
<img width="525" height="680" alt="image" src="https://github.com/user-attachments/assets/cdf74649-d92a-4518-b770-da93dddf60d0" />
<img width="475" height="667" alt="image" src="https://github.com/user-attachments/assets/18d7be1e-f47d-40d7-af45-733a3c977469" />
<img width="476" height="628" alt="image" src="https://github.com/user-attachments/assets/bf19edac-f2b4-475e-b673-c9dddb72943b" />
<img width="459" height="632" alt="image" src="https://github.com/user-attachments/assets/c227f7f8-6663-4827-a442-86a498521000" />
<img width="457" height="632" alt="image" src="https://github.com/user-attachments/assets/f182056d-6e92-4bb4-8d59-ecab46d0cc99" />
<img width="971" height="662" alt="image" src="https://github.com/user-attachments/assets/ce49d8b1-8011-4b91-ac4e-8151b00ddbe0" />

<h2>Firmware</h2>
<p>Coming soon</p>
<h2>Bill of Materials</h2>

|Name| Reference| Qty| Value| Sources|
|----------|----------|---|:-----:|:------:|
|Capacitors| C1-C3 & C5| 4| 10uF| [C15850](https://jlcpcb.com/partdetail/C15850)|
|| C4| 1| 1uF| [C28323](https://jlcpcb.com/partdetail/C28323)|
|| C6| 1| 2.2uF| [C377773](https://jlcpcb.com/partdetail/C377773)|
||  C7 & C8|  2|  4.7uF| [C1779](https://jlcpcb.com/partdetail/C1779)|
|| C11| 1| 0.1uF| [C49678](https://jlcpcb.com/partdetail/C49678)|
|Resistors| R1 & R2| 2| 5K1| [C27834](https://jlcpcb.com/partdetail/C27834)|
|| R3| 1| 34K8| [C2933423](https://jlcpcb.com/partdetail/C2933423)|
|| R4,R20 & R22| 3| 10K| [C17414](https://jlcpcb.com/partdetail/C17414)|
|| R5 & R8| 2| 27R| [C17594](https://jlcpcb.com/partdetail/C17594)|
|| R6 & R12| 2| 806K| [C2933502](https://jlcpcb.com/partdetail/C2933502)|
|| R7 & R13| 2| 2M| [C26112](https://jlcpcb.com/partdetail/C26112)|
|| R9 & R10| 2| 4K7| [C17673](https://jlcpcb.com/partdetail/C17673)|
|| R11| 1| 2K| [C17604](https://jlcpcb.com/partdetail/C17604)|
|| R19| 1| 24K9| [C17571](https://jlcpcb.com/partdetail/C17571)|
|| R21| 1| 20K| [C4328](https://jlcpcb.com/partdetail/C4328)|
|Diodes| D1-D82| 82| D| [C2099](https://jlcpcb.com/partdetail/C2099)|
|Keys| SW1-SW82| 82| Sockets| [C5333465](https://jlcpcb.com/partdetail/C5333465)|
|||>>|Switches|-|
|||>>|Key caps|-|
|SK6805 (LEDs)| D104-D185| 82| SK6805| [C2890035](https://jlcpcb.com/partdetail/C2890035)|
|ESDA5V3L (ESD protector for I2C lines)| D83| 1| ESDA5V3L| [C587142](https://jlcpcb.com/partdetail/C587142)|
|USB Connector| J1| 1| USB_C_Receptacle_USB2.0_14P| [C165948](https://jlcpcb.com/partdetail/C165948)|
|2x3 1mm PinHeader (SWD Interface)| J2| 1| Conn_02x03_Odd_Even| [C6837603](https://jlcpcb.com/partdetail/C6837603)|
|LTC4217 (Hotswap-controller)| U1| 1| LTC4217| [C687462](https://jlcpcb.com/partdetail/C687462)|
|USB6B1 (ESD protector for USB data lines)| U2| 1| USB6B1| [C283483](https://jlcpcb.com/partdetail/C283483)|
|MDBT50Q-1MV2 (MCU)| U3| 1| MDBT50Q-1MV2| [C5118826](https://jlcpcb.com/partdetail/C5118826)|
|LP2985-33DBVR (Voltage stabilizer/ 5V -> 3V3)| U4| 1| LP2985-3.3| [C95414](https://jlcpcb.com/partdetail/C95414)|
|MCP73831T-2ACI/OT | U5| 1| MCP73831-2-OT| [C424093](https://jlcpcb.com/partdetail/C424093)|
|1825232-1| U12| 1| 1825232-1| [C5167252](https://jlcpcb.com/partdetail/C5167252)|
|MT3608_Module (Boost converter/ 3V3 -> 5V)| U11| 1| MT3608_Module| [Link](https://www.aliexpress.com/item/1005006150124675.html)|
|| Conn1-Conn4| 4| Conn_01x06_Pin| [Link](https://www.aliexpress.com/item/1005007636554292.html)|

<h2>Keyboard Case</h2>
<p>coming soon</p>
