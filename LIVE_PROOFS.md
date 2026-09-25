# Live StudioNet proofs

Corrected contract: [0x0f817f9D6365535494C3b89Df43e78E18740D31A](https://explorer-studio.genlayer.com/address/0x0f817f9D6365535494C3b89Df43e78E18740D31A). Its deployed source was compared character-for-character with `contracts/AutonomousProtocolEvolution.py` after normalizing line endings. GenVM lint/SDK validation passed and four direct tests passed. Direct tests do not validate multi-validator behavior; the finalized StudioNet transactions below do.

| Step | Transaction | Verified result |
| --- | --- | --- |
| Corrected deployment | [0xe1fd9ba5…](https://explorer-studio.genlayer.com/tx/0xe1fd9ba5adb2120acef07c7ffda7f8bc88d74e0cd71ff6f5217dc2311051d25e) | FINALIZED; execution SUCCESS |
| Register hash-bound v0 | [0x44c1d617…](https://explorer-studio.genlayer.com/tx/0x44c1d61791dc780cfd4b0c64dca59348301a5e17a864b7ed8c9268d10f11d164) | FINALIZED; execution SUCCESS |
| Fetch/hash and activate v0 | [0x31419fd9…](https://explorer-studio.genlayer.com/tx/0x31419fd9d263b8a3542b284a148210f3125963354843b3b8c699d0ebfbd77e19) | FINALIZED; execution SUCCESS |
| Owner invites second wallet | [0xc0f1fb7d…](https://explorer-studio.genlayer.com/tx/0xc0f1fb7dc707ee938d1e75eb9f6a77d0f61f114e9906b0974a8432d80e91022c) | FINALIZED; execution SUCCESS |
| Invitee accepts | [0x77f429d0…](https://explorer-studio.genlayer.com/tx/0x77f429d0ef707a15ebce859b6d26d6a3c83994eb63128be42d026110b82ad3d0) | FINALIZED; execution SUCCESS |
| Invitee proposes additive v1 | [0x64c06e1a…](https://explorer-studio.genlayer.com/tx/0x64c06e1a4bb49de104bdcd777edc9d69642c8d49210cb84b05d8cea9cdbd2316) | FINALIZED; execution SUCCESS |
| Resolve additive proposal | [0xb48ed05e…](https://explorer-studio.genlayer.com/tx/0xb48ed05ef02a24afe4a992f53ff26998534f9b361c61b4144fc740eae8f38244) | FINALIZED; exact vector PASS/PASS/PASS/PASS; ACTIVATED version 1 |
| Invitee proposes breaking v2 | [0x86039424…](https://explorer-studio.genlayer.com/tx/0x86039424f23aa2a5bad8df18b66800c23959886b01670ad1e79ca3a73b103d6e) | FINALIZED; execution SUCCESS |
| Resolve breaking proposal | [0xff17028b…](https://explorer-studio.genlayer.com/tx/0xff17028bcccfee68b78388fbe8156f96792ad8e0d7dcef5d50ad12f3763a80b4) | FINALIZED; exact vector FAIL/FAIL/FAIL/PASS; INCOMPATIBLE, active version remains 1 |

The names of example files (v1/v2/v3) are documentation labels. The onchain version numbers are 0 for the baseline and 1 for the accepted additive successor; the breaking document never becomes an onchain version.

Both successful and rejected decisions include complete HTTP status, full-response SHA-256, hash-match and completeness fields in the onchain report. The additive root is `b0bea6edb933ab0a5a8a331b522ffb621ad0fb6286bec9f0a0a3f9eb33bd6921`; the breaking root is `37d48907ccde7a0e03bd9db7464263dc1775c18763e177fe4ea4a828a61a9fdb`.

The first deployment [0x8FE144Ae…](https://explorer-studio.genlayer.com/address/0x8FE144Aec80808C3bB2A903A6D51FE44232C59b2) is superseded. Its [invitation attempt](https://explorer-studio.genlayer.com/tx/0x17e348c7fc19b920d5a7468e64674434f24a54f58d85db6cb025f7df2f718149) finalized with an execution error due to double conversion of the decoded address argument. The corrected source and all results above are from the replacement deployment.
