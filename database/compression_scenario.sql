use au_bon_beurre;

select * from information_schema.tables where table_schema='au_bon_beurre';

SHOW VARIABLES WHERE Variable_name LIKE "have_%" OR Variable_name LIKE "%_compression_%";

-- select sleep(10); 

show status where variable_name in (
	'Innodb_page_compression_saved',
    'Innodb_page_compression_trim_sect512',
    'Innodb_page_compression_trim_sect1024',
    'Innodb_page_compression_trim_sect2048',
    'Innodb_page_compression_trim_sect4096',
    'Innodb_page_compression_trim_sect8192',
    'Innodb_page_compression_trim_sect16384',
    'Innodb_page_compression_trim_sect32768',
    'Innodb_num_pages_page_compressed',
    'Innodb_num_page_compressed_trim_op',
    'Innodb_num_page_compressed_trim_op_saved',
    'Innodb_num_pages_page_decompressed',
    'Innodb_num_pages_page_compression_error',
    'Innodb_have_lz4',
    'Innodb_have_lzon',
    'Innodb_have_lzma',
    'Innodb_have_bzip2',
    'Innodb_have_snappy'
)