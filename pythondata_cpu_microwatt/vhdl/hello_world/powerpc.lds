SECTIONS
{
	. = 0;
	_start = .;
	.head : {
		KEEP(*(.head))
	}
	. = 0x1000;
	.text : { *(.text) *(.text.*) *(.rodata) *(.rodata.*) }
	. = 0x1800;
	.data : { *(.data) *(.data.*) *(.got) *(.toc) }
	. = ALIGN(0x80);
	__bss_start = .;
	.bss : {
		*(.dynsbss)
		*(.sbss)
		*(.scommon)
		*(.dynbss)
		*(.bss)
		*(.common)
		*(.bss.*)
	}
	. = ALIGN(0x80);
	__bss_end = .;
	. = . + 0x2000;
	__stack_top = .;
}
