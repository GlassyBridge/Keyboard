<h1 align="center"> Wireless-Modular Keyboard </h1>
<div align="center">
  <img width="80%" alt="image" src="https://github.com/user-attachments/assets/3de422af-304e-4d5e-8017-280363eabc6f" />
</div>
<p align="center">This project is a custom modular keyboard that has both wireless and wired capabilities. It also uses low profile, kailh choc hotswap switches increasing customizability and its overall asthetic. Additionally, it offers magnetic connection following the I2C protocol which enables any type of module can connect to the main board securely.</p>
<h2></h2>
<h2> Features </h2>

- Works over USB-C (wired) or Bluetooth (wireless)
- Integrated magnetic pogo pins for stable I2C connection and adding external modules (numberpads, macropads or OLED modules)
- Integrated charging circuit for portability and wireless operation
- Uses Kailh Low Profile Choc hotswap sockets for key switch connections
- Features SK6805 addressable LEDs for customizable per key RGB lighting
- Includes a dedicated SWD interface for debugging and development
- A dedicated slide switch to manage battery life

<h2>Design</h2>
<h3>Schematic</h3>
<img width="49%" alt="Main_Board_Schematic" src="https://github.com/user-attachments/assets/00c6ecfa-7811-464e-bdc8-09416fe01dce" />
<img width="49%" alt="Keypad_Module_Schematic" src="https://github.com/user-attachments/assets/9988d776-ba61-45ed-a6f6-ed06badc78c9" />
<h4 align="center">Main board & Keypad</h4>
<h3>PCB</h3>

<img width="100%" alt="Back PCB" src="https://github.com/user-attachments/assets/0b47e930-3302-4fef-a9a6-45c70608f9eb" />
<h4 align="center">PCB back</h4>
<img width="100%" alt="Front PCB" src="https://github.com/user-attachments/assets/b39220f1-5d92-44de-ac83-3a20c1671a27" />
<h4 align="center">PCB front</h4>
<img width="100%" alt="PCB" src="https://github.com/user-attachments/assets/cedc6b69-ca47-4acc-819d-e210417ba209" />
<h4 align="center">PCB</h4>
<img width="100%" alt="No-Components 3D View" src="https://github.com/user-attachments/assets/4a15fb1a-3f6e-4260-aa9d-c4ff45b4fd4e" />
<h4 align="center">PCB 3D model</h4>
<img width="100%" alt="3D view" src="https://github.com/user-attachments/assets/8116f531-b872-41ad-8eeb-bf7f7235af24"/>
<h4 align="center">PCB 3D model with components</h4>

<h2>Firmware</h2>
<p>Coming soon</p>
<h2>Bill of Materials</h2>

| Name                     | Reference       |    Qty     | Unit Price ($) | moq | Shipping |                                            Link                                             |
| ------------------------ | --------------- | :--------: | -------------- | --- | -------- | :-----------------------------------------------------------------------------------------: |
| Capacitors (10uF)        | C1,C2,C5        |     3      | 0.016          | 20  | LCSC     |                  [C15850](https://www.lcsc.com/product-detail/C15850.html)                  |
| ---------- (1uF)         | C4              |     1      | 0.0099         | 20  | -        |                  [C28323](https://www.lcsc.com/product-detail/C28323.html)                  |
| ---------- (2.2uF)       | C6              |     1      | 0.02           | 20  | -        |                 [C377773](https://www.lcsc.com/product-detail/C377773.html)                 |
| ---------- (4.7uF)       | C7,C8           |     2      | 0.01           | 20  | -        |                   [C1779](https://www.lcsc.com/product-detail/C1779.html)                   |
| Diodes                   | D1-D82,D84-D103 |    102     | 0.009          | 150 | -        |                   [C2099](https://www.lcsc.com/product-detail/C2099.html)                   |
| ESDA5V3L                 | D83,D206        |     2      | 0.0382         | 10  | -        |                 [C587142](https://www.lcsc.com/product-detail/C587142.html)                 |
| SK6805 (LEDs)            | D104-D205       |    102     | 0.0722         | 105 | -        |                [C2890035](https://www.lcsc.com/product-detail/C2890035.html)                |
| USB Connector            | J1              |     1      | 0.1789         | 5   | -        |                 [C165948](https://www.lcsc.com/product-detail/C165948.html)                 |
| 2x3 1mm PinHeader        | J2              |     1      | 0.0312         | 20  | -        |                [C6837603](https://www.lcsc.com/product-detail/C6837603.html)                |
| Resistors  (5K1)         | R1,R2           |     2      | 0.0019         | 100 | -        |                  [C27834](https://www.lcsc.com/product-detail/C27834.html)                  |
| ---------- (10K)         | R14,R22         |     2      | 0.0022         | 100 | -        |                  [C17414](https://www.lcsc.com/product-detail/C17414.html)                  |
| ---------- (27R)         | R5,R8           |     2      | 0.0022         | 100 | -        |                  [C17594](https://www.lcsc.com/product-detail/C17594.html)                  |
| ---------- (806K)        | R6,R12,R15      |     3      | 0.002          | 100 | -        |                [C2933502](https://www.lcsc.com/product-detail/C2933502.html)                |
| ---------- (2M)          | R7,R13,R16      |     3      | 0.0028         | 100 | -        |                  [C26112](https://www.lcsc.com/product-detail/C26112.html)                  |
| ---------- (4K7)         | R9,R10,R17,R18  |     4      | 0.0019         | 100 | -        |                  [C17673](https://www.lcsc.com/product-detail/C17673.html)                  |
| ---------- (2K)          | R11             |     1      | 0.002          | 100 | -        |                  [C17604](https://www.lcsc.com/product-detail/C17604.html)                  |
| Keys ----- (Sockets)     | SW1-SW102       |    102     | 0.0963         | 100 | ??       |             [Aliexpress](https://www.aliexpress.com/item/1005005337309516.html)             |
| ---------- (Switches)    | -               |    102     | 50.78 (T)      | 110 | -        |             [Aliexpress](https://www.aliexpress.com/item/1005008883418065.html)             |
| ---------- (Key Caos)    | -               |    102     | 39.70 (T)      | -   | 6.00     |   [Chocfox](https://chosfox.com/products/chocfox-cfx-choc-keycaps?variant=42171505377474)   |
| ---------- (Stabilizers) | -               |     5      | 12.11 (T)      | -   | -        |               [Aliexpress](https://www.aliexpress.com/item/33039182740.html)                |
| USB6B1                   | U2              |     1      | 0.4738         | -   | -        |                 [C283483](https://www.lcsc.com/product-detail/C283483.html)                 |
| MCP73831T-2ACI/OT        | U5              |     1      | 0.7279         | -   | -        |                 [C424093](https://www.lcsc.com/product-detail/C424093.html)                 |
| MCP23017                 | U7              |     1      | 1.9493         | -   | -        |                 [C639770](https://www.lcsc.com/product-detail/C639770.html)                 |
| LP2985-33DBVR            | U4              |     1      | 0.1365         | 5   | -        |                  [C95414](https://www.lcsc.com/product-detail/C95414.html)                  |
| Slide switch (1825232-1) | U12             |     1      | 0.8335         |     | -        |                [C5167252](https://www.lcsc.com/product-detail/C5167252.html)                |
| XIAO-nRF52840-SMD (MCU)  | U6              |     1      | 9.90           |     | 3.75     |       [Seed Studio](https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html)        |
| MDBT50Q-1MV2 (MCU)       | U3              |     1      | 10.10          |     | >>       | [Seed Studio](https://www.seeedstudio.com/MDBT50Q-1M-nRF52840-Based-BLE-Module-p-3147.html) |
| MT3608_Module            | U11             |     1      | 0.99           |     | $1.99    |             [Aliexpress](https://www.aliexpress.com/item/1005008597901992.html)             |
| OLED Screen              | Brd11,Brd12     |     2      | 1.89           |     | $0.99    |             [Aliexpress](https://www.aliexpress.com/item/1005009242613187.html)             |
| 1X6 Magnetic Pogo Pins   | Conn1-Conn8     | 8(4 pairs) | 1.84           |     | $4.65    |             [Aliexpress](https://www.aliexpress.com/item/1005007636554292.html)             |
| lithium batteries        | -               |     2      | $9.03 (T)      |     | $5.43    |             [Aliexpress](https://www.aliexpress.com/item/1005010682559019.html)             |
| PCB                      | -               |     1      |                | 5   |          |                                                                                             |

<h2>Keyboard Case</h2>
<p>coming soon</p>
