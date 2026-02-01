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

| Name                                          | Reference       |  Qty  | Value                       | LCSC Part # | Unit Price ($) | moq | Shipping |                             Link                              |
| --------------------------------------------- | --------------- | :---: | --------------------------- | ----------- | -------------- | --- | -------- | :-----------------------------------------------------------: |
| Capacitors                                    | C1,C2,C5        |   3   | 10uF                        | C15850      | 0.016          | 20  | LCSC     |        [C15850](https://www.lcsc.com/product-detail/C15850.html)         |
|                                               | C4              |   1   | 1uF                         | C28323      | 0.0099         | 20  | -        |        [C28323](https://www.lcsc.com/product-detail/C28323.html)        |
|                                               | C6              |   1   | 2.2uF                       | C377773     | 0.02           | 20  | -        |       [C377773](https://www.lcsc.com/product-detail/C377773.html)        |
|                                               | C7,C8           |   2   | 4.7uF                       | C1779       | 0.01           | 20  | -        |         [C1779](https://www.lcsc.com/product-detail/C1779.html)          |
| Diodes                                        | D1-D82,D84-D103 |  102  | D                           | C2099       | 0.009          | 150 | -        |         [C2099](https://www.lcsc.com/product-detail/C2099.html)          |
| ESDA5V3L (ESD protector for I2C lines)        | D83,D206        |   2   | ESDA5V3L                    | C587142     | 0.0382         | 10  | -        |       [C587142](https://www.lcsc.com/product-detail/C587142.html)        |
| SK6805 (LEDs)                                 | D104-D205       |  102  | SK6805                      | C2890035    | 0.0722         | 105 | -        |      [C2890035](https://www.lcsc.com/product-detail/C2890035.html)       |
| USB Connector                                 | J1              |   1   | USB_C_Receptacle_USB2.0_14P | C165948     | 0.1789         | 5   | -        |       [C165948](https://www.lcsc.com/product-detail/C165948.html)        |
| 2x3 1mm PinHeader (SWD Interface)             | J2              |   1   | Conn_02x03_Odd_Even         | C6837603    | 0.0312         | 20  | -        |      [C6837603](https://www.lcsc.com/product-detail/C6837603.html)       |
| Resistors                                     | R1,R2           |   2   | 5K1                         | C27834      | 0.0019         | 100 | -        |        [C27834](https://www.lcsc.com/product-detail/C27834.html)         |
|                                               | R14,R22         |   2   | 10K                         | C17414      | 0.0022         | 100 | -        |        [C17414](https://www.lcsc.com/product-detail/C17414.html)         |
|                                               | R5,R8           |   2   | 27R                         | C17594      | 0.0022         | 100 | -        |        [C17594](https://www.lcsc.com/product-detail/C17594.html)         |
|                                               | R6,R12,R15      |   3   | 806K                        | C2933502    | 0.002          | 100 | -        |      [C2933502](https://www.lcsc.com/product-detail/C2933502.html)       |
|                                               | R7,R13,R16      |   3   | 2M                          | C26112      | 0.0028         | 100 | -        |        [C26112](https://www.lcsc.com/product-detail/C26112.html)         |
|                                               | R9,R10,R17,R18  |   4   | 4K7                         | C17673      | 0.0019         | 100 | -        |        [C17673](https://www.lcsc.com/product-detail/C17673.html)         |
|                                               | R11             |   1   | 2K                          | C17604      | 0.002          | 100 | -        |        [C17604](https://www.lcsc.com/product-detail/C17604.html)         |
| Keys                                          | SW1-SW102       |  102  | SW_Push (sockets)           | C5333465    | 0.0963         | 100 | ??       |      [Aliexpress](https://www.aliexpress.com/item/1005005337309516.html)       |
|                                               | -               |  102  | Switches                    |             | 50.78 (T)      | 110 | -       | [Aliexpress](https://www.aliexpress.com/item/1005008883418065.html)       |
|                                               | -               |  102  | Key caps                    |             | 39.70 (T)      |     | 6.00     | [Chocfox](https://chosfox.com/products/chocfox-cfx-choc-keycaps?variant=42171505377474)        |
|                                               | -               |   5   | Stabilizers                 |             | 12.11 (T)      |     | -     | [Aliexpress](https://www.aliexpress.com/item/33039182740.html) |
| USB6B1 (ESD protector for USB data lines)     | U2              |   1   | USB6B1                      | C283483     | 0.4738         |     | -        |       [C283483](https://www.lcsc.com/product-detail/C283483.html)        |
| MCP73831T-2ACI/OT                             | U5              |   1   | MCP73831-2-OT               | C424093     | 0.7279         |     | -        |       [C424093](https://www.lcsc.com/product-detail/C424093.html)        |
| MCP23017 (GPIO expander)                      | U7              |   1   | MCP23017_ML                 | C639770     | 1.9493         |     | -        |       [C639770](https://www.lcsc.com/product-detail/C639770.html)        |
| LP2985-33DBVR (Voltage stabilizer/ 5V -> 3V3) | U4              |   1   | LP2985-3.3                  | C95414      | 0.1365         | 5   | -        |        [C95414](https://www.lcsc.com/product-detail/C95414.html)         |
| Slide switch (1825232-1)                      | U12             |   1   | 1825232-1                   | C5167252    | 0.8335         |     | -        |      [C5167252](https://www.lcsc.com/product-detail/C5167252.html)       |
| XIAO-nRF52840-SMD (MCU)                       | U6              |   1   | XIAO-nRF52840-SMD           | C37327670   | 9.90           |     | 3.75     |   [Seed Studio](https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html)      |
| MDBT50Q-1MV2 (MCU)                            | U3              |   1   | MDBT50Q-1MV2                | C5118826    | 10.10          |     | >>       |      [Seed Studio](https://www.seeedstudio.com/MDBT50Q-1M-nRF52840-Based-BLE-Module-p-3147.html)       |
| MT3608_Module (Boost converter/ 3V3 -> 5V)    | U11             |   1   | MT3608_Module               |             | 0.99           |     | $1.99    | [Aliexpress](https://www.aliexpress.com/item/1005008597901992.html) |
| OLED Screen                                   | Brd11,Brd12     |   2   | SH1106                      |             | 1.89           |     | $0.99    | [Aliexpress](https://www.aliexpress.com/item/1005009242613187.html) |
| 1X6 Magnetic Pogo Pins                        | Conn1-Conn8     | 8(4 pairs) | Conn_01x06_Pin              |             | 1.84           |     | $4.65    | [Aliexpress](https://www.aliexpress.com/item/1005007636554292.html) |
| Rechargeable lithium batteries                | -               |   2   | 2000mah, 3V7 (2pc)          |             | $9.03          |     | $5.43    | [Aliexpress](https://www.aliexpress.com/item/1005010682559019.html) |

<h2>Keyboard Case</h2>
<p>coming soon</p>
