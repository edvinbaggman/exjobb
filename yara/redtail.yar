import "elf"

rule Detect_Redtail_Malware {
    meta:
        author = "Edvin Baggman"
        filetype = "ELF"
        date = "2024-05-06"
        malware = "REDTAIL"
        description = "YARA rule to detect Redtail cryptojacking malware"

    strings:
        $elf_magic = { 7f 45 4c 46 }
        $str_xmrig = "xmrig" nocase
        $entry_386 = { 31 ED 89 E0 83 E4 F0 50 50 E8 00 00 00 00 81 04 24 ?? ?? ?? 00 50 E8 00 00 00 00 55 57 56 53 81 EC 0C 01 00 00 8B 8C 24 20 01 00 00 8B 9C 24 24 01 00 00 8B 01 40 8B 74 81 04 89 C2 40 85 F6 75 F5 8D 54 91 08 31 C0 C7 04 84 00 00 00 00 40 83 F8 20 75 F3 8B 02 85 C0 74 10 83 F8 1F 77 06 8B 72 04 89 34 }
        $entry_AMD64 = { 48 31 ED 48 89 E7 48 8D 35 ?? ?? ?? 00 48 83 E4 F0 E8 00 00 00 00 48 81 EC 90 01 00 00 8B 07 49 89 F8 48 89 F1 FF C0 48 98 49 8B 74 C0 08 48 89 C2 48 FF C0 48 85 F6 75 F0 49 8D 54 D0 10 31 C0 48 C7 44 C4 88 00 00 00 00 48 FF C0 48 83 F8 20 75 EE 48 8B 02 48 85 C0 74 15 48 83 F8 1F 77 09 48 8B 72 08 }
        $entry_ARM = { 00 B0 A0 E3 00 E0 A0 E3 10 10 9F E5 01 10 8F E0 0D 00 A0 E1 0F C0 C0 E3 0C D0 A0 E1 15 00 00 EB ?? ?? ?? 00 07 40 2D E9 00 C0 A0 E3 34 20 9F E5 34 30 9F E5 34 00 9F E5 02 20 8F E0 03 30 92 E7 00 00 92 E7 04 C0 8D E5 24 C0 9F E5 0C 20 92 E7 00 20 8D E5 04 20 81 E2 00 10 91 E5 ?? ?? ?? EB 0C D0 8D E2 }
        $entry_AARCH64 = { 1D 00 80 D2 1E 00 80 D2 E0 03 00 91 ?1 21 00 ?0 21 ?0 2? 91 1F EC 7C 92 0B 00 00 14 E2 03 01 AA ?4 21 00 ?0 ?3 21 00 ?0 ?0 21 00 ?0 84 ?? 47 F9 05 00 80 D2 63 B? 47 F9 00 A? 47 F9 41 84 40 F8 ?? ?? 0B 14 E4 03 00 AA FF 03 08 D1 02 84 40 F8 42 04 00 11 42 7C 40 93 03 78 62 F8 42 04 00 91 C3 FF FF B5 }
    condition:
        $elf_magic at 0 and 
        $str_xmrig and
        any of ($entry_*) at elf.entry_point
}