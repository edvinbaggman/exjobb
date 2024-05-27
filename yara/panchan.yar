
rule Detect_Panchan_Malware {
    meta:
        author = "Edvin Baggman"
        filetype = "ELF"
        date = "2024-05-06"
        malware = "PANCHAN"
        description = "YARA rule to detect Panchan cryptojacking malware"

    strings:
        $elf_magic = { 7f 45 4c 46 }
        $golang = "goroutine"
        $hex_panchan_header =  { 70 61 6E 2D 63 68 61 6E 27 73 20 6D 69 6E 69 6E 67 20 [0-10] 20 68 69 21} // pan-chan's mining _ hi!
        $base64_table = { 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F 50 51 52 53 54 55 56 57 58 59 5A 61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F 70 71 72 73 74 75 76 77 78 79 7A 30 31 32 33 34 35 36 37 38 39 2B 2F }
        $str_nbminer = "nbminer" nocase
	    $str_xmrig = "xmrig" nocase

    condition:
        all of them and $elf_magic at 0
}