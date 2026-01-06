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
<h2>Design - Keypad module</h2>
<h3>Schematic</h3>
<img width="100%" alt="K-schematic" src="https://github.com/user-attachments/assets/ce49d8b1-8011-4b91-ac4e-8151b00ddbe0" />
<h3>PCB</h3>
<img width="50%" alt="PCB" src="https://github.com/user-attachments/assets/bf19edac-f2b4-475e-b673-c9dddb72943b" />
<h4 align="center">PCB</h4>
<img width="50%" alt="PCB-front" src="https://github.com/user-attachments/assets/c227f7f8-6663-4827-a442-86a49852500" />
<h4 align="center">PCB front</h4>
<img width="50%" alt="PCB-back" src="https://github.com/user-attachments/assets/f182056d-6e92-4bb4-8d59-ecab46d0cc99" />
<h4 align="center">PCB back</h4>
<img width="50%" alt="3D model with components" src="https://github.com/user-attachments/assets/cdf74649-d92a-4518-b770-da93dddf60d0" />
<h4 align="center">PCB 3D model with components</h4>
<img width="50%" alt="3D model" src="https://github.com/user-attachments/assets/18d7be1e-f47d-40d7-af45-733a3c977469" />
<h4 align="center">PCB 3D model</h4>

<h2>Firmware</h2>
<p>Coming soon</p>
<h2>Bill of Materials</h2>

| Name                                          | Reference              |  Qty  | Value                       | LCSC Part # | Unit Price ($) | moq | Shipping |                             Link                              |
| --------------------------------------------- | ---------------------- | :---: | --------------------------- | ----------- | -------------- | --- | -------- | :-----------------------------------------------------------: |
| Capacitors                                    | C1-C3,C5,C13           |   5   | 10uF                        | C15850      | 0.01           |     | PCBA     |        [C15850](https://jlcpcb.com/partdetail/C15850)         |
|                                               | C4                     |   1   | 1uF                         | C28323      | 0.01           |     | -        |        [C28323](https://jlcpcb.com/partdetail/C28323)         |
|                                               | C6                     |   1   | 2.2uF                       | C377773     | 0.02           |     | -        |       [C377773](https://jlcpcb.com/partdetail/C377773)        |
|                                               | C7,C8                  |   2   | 4.7uF                       | C1779       | 0.01           |     | -        |         [C1779](https://jlcpcb.com/partdetail/C1779)          |
|                                               | C11,C12                |   2   | 0.1uF                       | C49678      | 0.01           |     | -        |        [C49678](https://jlcpcb.com/partdetail/C49678)         |
| Diodes                                        | D1-D82,D84-D103        |  102  | D                           | C2099       | 0.01           |     | -        |         [C2099](https://jlcpcb.com/partdetail/C2099)          |
| ESDA5V3L (ESD protector for I2C lines)        | D83,D206               |   2   | ESDA5V3L                    | C587142     | 0.04           |     | -        |       [C587142](https://jlcpcb.com/partdetail/C587142)        |
| SK6805 (LEDs)                                 | D104-D205              |  102  | SK6805                      | C2890035    | 0.10           |     | -        |      [C2890035](https://jlcpcb.com/partdetail/C2890035)       |
| USB Connector                                 | J1                     |   1   | USB_C_Receptacle_USB2.0_14P | C165948     | 0.18           |     | -        |       [C165948](https://jlcpcb.com/partdetail/C165948)        |
| 2x3 1mm PinHeader (SWD Interface)             | J2                     |   1   | Conn_02x03_Odd_Even         | C6837603    | 0.03           |     | -        |      [C6837603](https://jlcpcb.com/partdetail/C6837603)       |
| Resistors                                     | R1,R2                  |   2   | 5K1                         | C27834      | 0.01           |     | -        |        [C27834](https://jlcpcb.com/partdetail/C27834)         |
|                                               | R3,R25                 |   2   | 34K8                        | C2933423    | 0.01           |     | -        |      [C2933423](https://jlcpcb.com/partdetail/C2933423)       |
|                                               | R4,R14,R20,R22,R24,R27 |   6   | 10K                         | C17414      | 0.01           |     | -        |        [C17414](https://jlcpcb.com/partdetail/C17414)         |
|                                               | R5,R8                  |   2   | 27R                         | C17594      | 0.01           |     | -        |        [C17594](https://jlcpcb.com/partdetail/C17594)         |
|                                               | R6,R12,R15             |   3   | 806K                        | C2933502    | 0.01           |     | -        |      [C2933502](https://jlcpcb.com/partdetail/C2933502)       |
|                                               | R7,R13,R16             |   3   | 2M                          | C26112      | 0.01           |     | -        |        [C26112](https://jlcpcb.com/partdetail/C26112)         |
|                                               | R9,R10,R17,R18         |   4   | 4K7                         | C17673      | 0.01           |     | -        |        [C17673](https://jlcpcb.com/partdetail/C17673)         |
|                                               | R11                    |   1   | 2K                          | C17604      | 0.01           |     | -        |        [C17604](https://jlcpcb.com/partdetail/C17604)         |
|                                               | R19,R23                |   2   | 24K9                        | C17571      | 0.01           |     | -        |        [C17571](https://jlcpcb.com/partdetail/C17571)         |
|                                               | R21,R26                |   2   | 20K                         | C4328       | 0.01           |     | -        |         [C4328](https://jlcpcb.com/partdetail/C4328)          |
| Keys                                          | SW1-SW102              |  102  | SW_Push                     | C5333465    | 0.1213         | 73  | -        |      [C5333465](https://jlcpcb.com/partdetail/C5333465)       |
|                                               | -                      |  102  | Switches                    |             |                |     | -        | [Link](https://www.aliexpress.com/item/1005005883472162.html) |
|                                               | -                      |  102  | Key caps                    |             |                |     | -        |                               -                               |
| LTC4217 (Hotswap-controller)                  | U1,U13                 |   2   | LTC4217                     | C687462     | 11.90          |     | -        |       [C687462](https://jlcpcb.com/partdetail/C687462)        |
| USB6B1 (ESD protector for USB data lines)     | U2                     |   1   | USB6B1                      | C283483     | 0.4702         | 19  | -        |       [C283483](https://jlcpcb.com/partdetail/C283483)        |
| MDBT50Q-1MV2 (MCU)                            | U3                     |   1   | MDBT50Q-1MV2                | C5118826    | 6.9468         | 2   | -        |      [C5118826](https://jlcpcb.com/partdetail/C5118826)       |
| LP2985-33DBVR (Voltage stabilizer/ 5V -> 3V3) | U4                     |   1   | LP2985-3.3                  | C95414      | 0.12           |     | -        |        [C95414](https://jlcpcb.com/partdetail/C95414)         |
| MCP73831T-2ACI/OT                             | U5                     |   1   | MCP73831-2-OT               | C424093     | 0.72           |     | -        |       [C424093](https://jlcpcb.com/partdetail/C424093)        |
| MCP23017 (GPIO expander)                      | U7                     |   1   | MCP23017_ML                 | C639770     | 1.93           |     | -        |       [C639770](https://jlcpcb.com/partdetail/C639770)        |
| Slide switch (1825232-1)                      | U12                    |   1   | 1825232-1                   | C5167252    | 0.84           |     | -        |      [C5167252](https://jlcpcb.com/partdetail/C5167252)       |
| XIAO-nRF52840-SMD (MCU)                       | U6                     |   1   | XIAO-nRF52840-SMD           | C37327670   | 0.0196         | 447 | -        |     [C37327670](https://jlcpcb.com/partdetail/C37327670)      |
| MT3608_Module (Boost converter/ 3V3 -> 5V)    | U11                    |   1   | MT3608_Module               |             | 0.99           |     | $1.99    | [Link](https://www.aliexpress.com/item/1005008597901992.html) |
| OLED Screen                                   | Brd11,Brd12            |   2   | SH1106                      |             | 1.89           |     | $0.99    | [Link](https://www.aliexpress.com/item/1005009242613187.html) |
| 1X6 Magnetic Pogo Pins                        | Conn1-Conn8            |   8   | Conn_01x06_Pin              |             | 1.84           |     | $4.65    | [Link](https://www.aliexpress.com/item/1005007636554292.html) |
| Rechargeable lithium batteries                | -                      |   2   | 2000mah, 3V7 (2pc)          |             | $9.03          |     | $5.43    | [Link](https://www.aliexpress.com/item/1005010682559019.html) |


<!-- Main board -->
<details>
  <summary>Main-board</summary>
  <h3 align="center">Main-board</h3>

  --------------
  | Name                                          | Reference    |  Qty |            Value            |                            Sources                            |
  | --------------------------------------------- | ------------ | ---: | :-------------------------: | :-----------------------------------------------------------: |
  | Capacitors                                    | C1-C3 & C5   |    4 |            10uF             |        [C15850](https://jlcpcb.com/partdetail/C15850)         |
  |                                               | C4           |    1 |             1uF             |        [C28323](https://jlcpcb.com/partdetail/C28323)         |
  |                                               | C6           |    1 |            2.2uF            |       [C377773](https://jlcpcb.com/partdetail/C377773)        |
  |                                               | C7 & C8      |    2 |            4.7uF            |         [C1779](https://jlcpcb.com/partdetail/C1779)          |
  |                                               | C11          |    1 |            0.1uF            |        [C49678](https://jlcpcb.com/partdetail/C49678)         |
  | Resistors                                     | R1 & R2      |    2 |             5K1             |        [C27834](https://jlcpcb.com/partdetail/C27834)         |
  |                                               | R3           |    1 |            34K8             |      [C2933423](https://jlcpcb.com/partdetail/C2933423)       |
  |                                               | R4,R20 & R22 |    3 |             10K             |        [C17414](https://jlcpcb.com/partdetail/C17414)         |
  |                                               | R5 & R8      |    2 |             27R             |        [C17594](https://jlcpcb.com/partdetail/C17594)         |
  |                                               | R6 & R12     |    2 |            806K             |      [C2933502](https://jlcpcb.com/partdetail/C2933502)       |
  |                                               | R7 & R13     |    2 |             2M              |        [C26112](https://jlcpcb.com/partdetail/C26112)         |
  |                                               | R9 & R10     |    2 |             4K7             |        [C17673](https://jlcpcb.com/partdetail/C17673)         |
  |                                               | R11          |    1 |             2K              |        [C17604](https://jlcpcb.com/partdetail/C17604)         |
  |                                               | R19          |    1 |            24K9             |        [C17571](https://jlcpcb.com/partdetail/C17571)         |
  |                                               | R21          |    1 |             20K             |         [C4328](https://jlcpcb.com/partdetail/C4328)          |
  | Diodes                                        | D1-D82       |   82 |              D              |         [C2099](https://jlcpcb.com/partdetail/C2099)          |
  | ESDA5V3L (ESD protector for I2C lines)        | D83          |    1 |          ESDA5V3L           |       [C587142](https://jlcpcb.com/partdetail/C587142)        |
  | SK6805 (LEDs)                                 | D104-D185    |   82 |           SK6805            |      [C2890035](https://jlcpcb.com/partdetail/C2890035)       |
  | Keys                                          | SW1-SW82     |   82 |           Sockets           |      [C5333465](https://jlcpcb.com/partdetail/C5333465)       |
  |                                               |              |   82 |          Switches           | [Link](https://www.aliexpress.com/item/1005005883472162.html) |
  |                                               |              |   82 |          Key caps           |                               -                               |
  | USB Connector                                 | J1           |    1 | USB_C_Receptacle_USB2.0_14P |       [C165948](https://jlcpcb.com/partdetail/C165948)        |
  | 2x3 1mm PinHeader (SWD Interface)             | J2           |    1 |     Conn_02x03_Odd_Even     |      [C6837603](https://jlcpcb.com/partdetail/C6837603)       |
  | LTC4217 (Hotswap-controller)                  | U1           |    1 |           LTC4217           |       [C687462](https://jlcpcb.com/partdetail/C687462)        |
  | USB6B1 (ESD protector for USB data lines)     | U2           |    1 |           USB6B1            |       [C283483](https://jlcpcb.com/partdetail/C283483)        |
  | MDBT50Q-1MV2 (MCU)                            | U3           |    1 |        MDBT50Q-1MV2         |      [C5118826](https://jlcpcb.com/partdetail/C5118826)       |
  | LP2985-33DBVR (Voltage stabilizer/ 5V -> 3V3) | U4           |    1 |         LP2985-3.3          |        [C95414](https://jlcpcb.com/partdetail/C95414)         |
  | MCP73831T-2ACI/OT                             | U5           |    1 |        MCP73831-2-OT        |       [C424093](https://jlcpcb.com/partdetail/C424093)        |
  | 1825232-1                                     | U12          |    1 |          1825232-1          |      [C5167252](https://jlcpcb.com/partdetail/C5167252)       |
  | MT3608_Module (Boost converter/ 3V3 -> 5V)    | U11          |    1 |        MT3608_Module        | [Link](https://www.aliexpress.com/item/1005008597901992.html) |
  | 1X6 Magnetic Pogo Pins                        | Conn1-Conn4  |    4 |       Conn_01x06_Pin        | [Link](https://www.aliexpress.com/item/1005007636554292.html) |
  ----------
</details>

<details>
<summary>Key-pad module</summary>
<h3 align="center">Key pad module</h3>

----------
| Name                         | Reference      |  Qty |       Value       |                            Comment                            |
| ---------------------------- | -------------- | ---: | :---------------: | :-----------------------------------------------------------: |
| Capacitors                   | C12            |    1 |       0.1uF       |        [C49678](https://jlcpcb.com/partdetail/C49678)         |
|                              | C13            |    1 |       10uF        |        [C15850](https://jlcpcb.com/partdetail/C15850)         |
| Resistors                    | R23            |    1 |       24K9        |        [C17571](https://jlcpcb.com/partdetail/C17571)         |
|                              | R14, R24 & R27 |    3 |        10K        |        [C17414](https://jlcpcb.com/partdetail/C17414)         |
|                              | R25            |    1 |       34K8        |      [C2933423](https://jlcpcb.com/partdetail/C2933423)       |
|                              | R26            |    1 |        20K        |         [C4328](https://jlcpcb.com/partdetail/C4328)          |
|                              | R17,R18        |    2 |        4K7        |        [C17673](https://jlcpcb.com/partdetail/C17673)         |
|                              | R16            |    1 |        2M         |        [C26112](https://jlcpcb.com/partdetail/C26112)         |
|                              | R15            |    1 |       806K        |      [C2933502](https://jlcpcb.com/partdetail/C2933502)       |
| Diodes                       | D84-D103       |   20 |         D         |         [C2099](https://jlcpcb.com/partdetail/C2099)          |
| ESD5V3L                      | D206           |    1 |     ESDA5V3L      |       [C587142](https://jlcpcb.com/partdetail/C587142)        |
| SK6805 (LEDs)                | D186–D205      |   20 |      SK6805       |      [C2890035](https://jlcpcb.com/partdetail/C2890035)       |
| Keys                         | SW83-SW102     |   20 |      Sockets      |      [C5333465](https://jlcpcb.com/partdetail/C5333465)       |
|                              |                |   20 |     Switches      | [Link](https://www.aliexpress.com/item/1005005883472162.html) |
|                              |                |   20 |     Key Caps      |                                                               |
| LTC4217 (Hotswap controller) | U13            |    1 |      LTC4217      |       [C687462](https://jlcpcb.com/partdetail/C687462)        |
| MCP23017                     | U7             |    1 |    MCP23017_ML    |       [C639770](https://jlcpcb.com/partdetail/C639770)        |
| XIAO-nRF52840-SMD            | U6             |    1 | XIAO-nRF52840-SMD |     [C37327670](https://jlcpcb.com/partdetail/C37327670)      |
| 1X6 Magnetic Pogo Pin        | Conn5-Conn8    |    4 |  Conn_01x06_Pin   | [Link](https://www.aliexpress.com/item/1005007636554292.html) |
| OLED screen                  | Brd11 & Brd12  |    2 |      SH1106       |                            [Link]                             |
</details>

<h2>Keyboard Case</h2>
<p>coming soon</p>
