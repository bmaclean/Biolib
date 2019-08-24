# Format Package

## Format.fasta

The fasta module is used for read/write operations involing fasta files.

**`fasta.from_fasta(fasta_file)`**

`fasta_file` - the Fasta file to be parsed into a useable data structure.

### Example

To parse the file `cubilin.fasta`:

```fasta
>sp|O60494|CUBN_HUMAN Cubilin OS=Homo sapiens GN=CUBN PE=1 SV=5
MMNMSLPFLWSLLTLLIFAEVNGEAGELELQRQKRSINLQQPRMATERGNLVFLTGSAQN
IEFRTGSLGKIKLNDEDLSECLHQIQKNKEDIIELKGSAIGLPQNISSQIYQLNSKLVDL
ERKFQGLQQTVDKKVCSSNPCQNGGTCLNLHDSFFCICPPQWKGPLCSADVNECEIYSGT
...
```

```python
cubilin_fasta = open('../cubilin.fasta')
cubilin = fasta.from_fasta(cubilin_fasta)
```

Returns a dict of the format:

```python
{
    header: 'gi|5524211|gb|AAD44166.1| cytochrome b [Elephas maximus maximus]',
    sequence: 'LCLYTHIGRNIYYGSYLYSETWNTGIMLLLITMATAFMGYVLPWGQMSFWGATVITNLFSAIPYIGTNLVEWIWGGFSVDKATLNRFFAFHFILPFTMVALAGVHLTFLHETGSNNPLGLTSDSDKIPFHPYYTIKDFLGLLILILLLLLLALLSPDMLGDPDNHMPADPLNTPLHIKPEWYFLFAYAILRSVPNKLGGVLALFLSIVILGLMPFLHTSKHRSMMLRPLSQALFWTLTMDLLTLTWIGSQPVEYPYTIIGQMASILYFSIILAFLPIAGXIENY'
}
```

**`fasta.to_fasta(source, target)`**
