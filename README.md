<h1 align="center"> Wireless-Modular Keyboard </h1>
<div align="center">
  <img width="80%" alt="image" src="https://github.com/user-attachments/assets/d57b7f7e-3add-4d3c-9f40-f51e95c1a49f" />
</div>
<p align="center">A custom modular keyboard that has both wireless and wired capabilities, uses MX hotswap switches (with per key RGB lighting) and a magnetic pogo pin connection which follows the I2C protocol.</p>
<h2></h2>
<h2> Features </h2>

- Works over USB-C (wired) or Bluetooth (wireless)
- Integrated magnetic pogo pins for stable I2C connection and adding external modules (numberpads, macropads or OLED modules)
- Integrated charging circuit for portability and wireless operation
- Uses MX hotswap sockets for key switch connections
- Features SK6812MINI-E back mounted LEDs for customizable per key RGB lighting
- Includes a dedicated SWD interface for debugging and development
- A dedicated slide switch to manage battery life

<h2>Design</h2>
<h3>Schematic</h3>
<img width="49%" alt="Main_Board_Schematic" src="https://github.com/user-attachments/assets/85a9a515-3020-464d-8725-8060c9dc251d" />
<img width="49%" alt="Keypad_Module_Schematic" src="https://github.com/user-attachments/assets/9ba47d6a-d990-400c-a9e0-5136f25dfe45" />
<h4 align="center">Main board & Keypad</h4>
<h3>PCB</h3>
<img width="100%" alt="Back PCB" src="https://github.com/user-attachments/assets/cbfe85f1-cb7f-49a8-94bf-5b7986f6b4df" />
<h4 align="center">PCB back</h4>
<img width="100%" alt="Front PCB" src="https://github.com/user-attachments/assets/1025c5e5-272c-4dad-88c7-d39d3891780f" />
<h4 align="center">PCB front</h4>
<img width="100%" alt="PCB" src="https://github.com/user-attachments/assets/8e6a50c4-5f36-48c2-8e3a-505326f94985" />
<h4 align="center">PCB</h4>
<img width="100%" alt="No-Components 3D View front" src="https://github.com/user-attachments/assets/6a199f89-a3b4-4a0d-b39f-cf482c37a095" />
<img width="100%" alt="No-Components 3D View back" src="https://github.com/user-attachments/assets/267f41db-41f7-4835-a930-d3e896748e78" />
<h4 align="center">PCB 3D model</h4>
<img width="100%" alt="3D view front" src="https://github.com/user-attachments/assets/c0105391-5848-4349-84f0-9c8bddb8ab07"/>
<img width="100%" alt="3D view back" src="https://github.com/user-attachments/assets/c5e5cc9f-e2c7-4141-980e-54427c0cc2eb"/>
<h4 align="center">PCB 3D model with components</h4>

<h2>Firmware</h2>

Available in the `Firmware` folder. (Basic version for now. I'll update it once I built the keyboard)
<h2>Bill of Materials</h2>

| Name                     | Reference   |    Qty     | moq | Price ($) | Shipping |                                            Link                                             |
| ------------------------ | ----------- | :--------: | --- | --------- | -------- | :-----------------------------------------------------------------------------------------: |
| OLED Screens (128X32)    | Brd11       |     1      | 1   | 1.54      | -        |             [Aliexpress](https://www.aliexpress.com/item/1005006913366977.html)             |
| ------------ (128X64)    | Brd12       |     1      | 1   | 2.94      | -        |             [Aliexpress](https://www.aliexpress.com/item/1005009242613187.html)             |
| Capacitors (10uF)        | C1-C4       |     4      | 20  | 0.43      | LCSC     |                  [C15850](https://www.lcsc.com/product-detail/C15850.html)                  |
| ---------- (4.7uF)       | C5,C6       |     2      | 20  | 0.29      | LCSC     |                   [C1779](https://www.lcsc.com/product-detail/C1779.html)                   |
| ---------- (22uF)        | C7,C8       |     2      | 20  | 1.12      | LCSC     |                  [C12891](https://www.lcsc.com/product-detail/C12891.html)                  |
| 1X6 Magnetic Pogo Pins   | Conn1-Conn8 | 8(4 pairs) | 1   | 1.82      | -        |             [Aliexpress](https://www.aliexpress.com/item/1005007636554292.html)             |
| Diodes                   | D1-D99      |     99     | 100 | 0.93      | LCSC     |                   [C2099](https://www.lcsc.com/product-detail/C2099.html)                   |
| ---------- (SS34)        | SS34        |     1      | 20  | 0.56      | LCSC     |                 [C908680](https://www.lcsc.com/product-detail/C908680.html)                 |
| ESDA5V3L                 | ESD1,ESD2   |     2      | 10  | 0.39      | LCSC     |                 [C587142](https://www.lcsc.com/product-detail/C587142.html)                 |
| USB Connector            | J1          |     1      | 5   | 0.84      | LCSC     |                 [C165948](https://www.lcsc.com/product-detail/C165948.html)                 |
| 2x3 1mm PinHeader        | J2          |     1      | 20  | 0.65      | LCSC     |                [C6837603](https://www.lcsc.com/product-detail/C6837603.html)                |
| Inductors  (10uH)        | L1          |     1      | 10  | 0.47      | LCSC     |                  [C88173](https://www.lcsc.com/product-detail/C88173.html)                  |
| ---------- (22uH)        | L2          |     1      | 5   | 0.83      | LCSC     |                  [C27442](https://www.lcsc.com/product-detail/C27442.html)                  |
| SK6812MINI-E (LEDs)      | LED1-LED99  |     99     | 100 | 7.45      | LCSC     |                [C5149201](https://www.lcsc.com/product-detail/C5149201.html)                |
| P_Mosfets                | Q1-Q3       |     3      | 10  | 0.65      | LCSC     |                  [C10487](https://www.lcsc.com/product-detail/C10487.html)                  |
| Resistors  (110K)        | R1          |     2      | 100 | 0.19      | LCSC     |                [C2907221](https://www.lcsc.com/product-detail/C2907221.html)                |
| ---------- (5K1)         | R2,R4       |     2      | 100 | 0.24      | LCSC     |                  [C27834](https://www.lcsc.com/product-detail/C27834.html)                  |
| ---------- (100K)        | R3,R5,R6    |     2      | 100 | 0.22      | LCSC     |                [C2933502](https://www.lcsc.com/product-detail/C2933502.html)                |
| ---------- (4K7)         | R7,R12,R18  |     4      | 100 | 0.19      | LCSC     |                  [C17673](https://www.lcsc.com/product-detail/C17673.html)                  |
| ---------- (27R)         | R8,R11      |     2      | 100 | 0.22      | LCSC     |                  [C17594](https://www.lcsc.com/product-detail/C17594.html)                  |
| ---------- (806K)        | R9,R16,R21  |     3      | 100 | 0.22      | LCSC     |                [C2933502](https://www.lcsc.com/product-detail/C2933502.html)                |
| ---------- (2M)          | R10,R17,R22 |     3      | 100 | 0.30      | LCSC     |                  [C26112](https://www.lcsc.com/product-detail/C26112.html)                  |
| ---------- (15K)         | R13         |     1      | 100 | 0.21      | LCSC     |                [C2930170](https://www.lcsc.com/product-detail/C2930170.html)                |
| ---------- (10K)         | R14,R19     |     2      | 100 | 0.25      | LCSC     |                  [C17414](https://www.lcsc.com/product-detail/C17414.html)                  |
| ---------- (2K)          | R15         |     1      | 100 | 0.25      | LCSC     |                  [C17604](https://www.lcsc.com/product-detail/C17604.html)                  |
| ======================   | =========== | ========== | === | =======   | =======  |                                              =                                              |
| Rotary Encoder           | RE1         |     1      | 1   | 1.87      | LCSC     |                 [C470742](https://www.lcsc.com/product-detail/C470742.html)                 |
| Slide switch (1825232-1) | SPDT1       |     1      | 1   | 0.93      | LCSC     |                [C5167252](https://www.lcsc.com/product-detail/C5167252.html)                |
| Keys ----- (Sockets)     | SW1-SW99    |     99     | 100 | 12.14     | -        |             [Aliexpress](https://www.aliexpress.com/item/1005005337309516.html)             |
| ---------- (Switches)    | -           |     99     | 110 | 50.78 (T) | LCSC     |             [Aliexpress](https://www.aliexpress.com/item/1005008883418065.html)             |
| ---------- (Key Caps)    | -           |     99     | 1   | 39.70 (T) | -        |   [Chocfox](https://chosfox.com/products/chocfox-cfx-choc-keycaps?variant=42171505377474)   |
| ---------- (Stabilizers) | -           |     5      | 1   | 12.11 (T) | LCSC     |               [Aliexpress](https://www.aliexpress.com/item/33039182740.html)                |
| ======================   | =========== | ========== | === | =======   | =======  |                                              =                                              |
| MT3608                   | U1          |     1      | 10  | 0.79      | LCSC     |                  [C84817](https://www.lcsc.com/product-detail/C84817.html)                  |
| USB6B1                   | U2          |     1      | 1   | 0.47      | LCSC     |                 [C283483](https://www.lcsc.com/product-detail/C283483.html)                 |
| MDBT50Q-1MV2 (MCU)       | U3          |     1      | 1   | 10.10     | SEED     | [Seed Studio](https://www.seeedstudio.com/MDBT50Q-1M-nRF52840-Based-BLE-Module-p-3147.html) |
| MCP73831T-2ACI/OT        | U4          |     1      | 1   | 0.74      | LCSC     |                 [C424093](https://www.lcsc.com/product-detail/C424093.html)                 |
| XIAO-nRF52840-SMD (MCU)  | U5          |     1      | 1   | 9.90      | 3.75     |       [Seed Studio](https://www.seeedstudio.com/Seeed-XIAO-BLE-nRF52840-p-5201.html)        |
| MCP23017                 | U6          |     1      | 1   | 2.03      | LCSC     |                 [C639770](https://www.lcsc.com/product-detail/C639770.html)                 |
| 74LV1T08GV               | U7,U8       |     2      | 1   | 2.12      | LCSC     |                 [C547934](https://www.lcsc.com/product-detail/C547934.html)                 |
| lithium batteries        | -           |     2      | -   | $9.03 (T) | $5.43    |             [Aliexpress](https://www.aliexpress.com/item/1005010682559019.html)             |

> *T for total price

<h2>Keyboard Case</h2>

A very basic case is provided in the `CAD` folder.


<img width="100%" alt="image" src="https://github.com/user-attachments/assets/dcbb5de1-e0c6-4394-a4bc-7c58d07d5797" />

