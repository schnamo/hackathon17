# use this script by setting CONTEXT=context length
BEGIN {}
{
	pos = $1;
	ml = $2;
	motif = $4;
	len = length(motif);
	if (len-CONTEXT*2 < ml) {
		if (pos+0 < CONTEXT) {
			s1 = substr(motif, 1, len-CONTEXT-ml);
			if (length(s1) == 0) s1 = "X"
			s2 = substr(motif, length(s1)+1, ml);
			s3 = substr(motif, len-CONTEXT+1);
		} else {   #if (pos+0 > LENGTH-CONTEXT) 
			s1 = substr(motif, 1, CONTEXT);
			s2 = substr(motif, length(s1)+1, ml);
			s3 = substr(motif, length(s2)+CONTEXT+1);
			if (length(s3) == 0) s3 = "X"
		}
	} else {
			s1 = substr(motif, 1, CONTEXT);
			s2 = substr(motif, length(s1)+1, ml);
			s3 = substr(motif, len-CONTEXT+1);
	}
	printf("%d %d %s %s %s",pos,pos+ml,s1,s2,s3);

	pos = $5;
	ml = $6;
	motif = $8;
	len = length(motif);
	if (len-CONTEXT*2 < ml) {
		if (pos+0 < CONTEXT) {
			s1 = substr(motif, 1, len-CONTEXT-ml);
			if (length(s1) == 0) s1 = "X"
			s2 = substr(motif, length(s1)+1, ml);
			s3 = substr(motif, len-CONTEXT+1);
		} else {   #if (pos+0 > LENGTH-CONTEXT) 
			s1 = substr(motif, 1, CONTEXT);
			s2 = substr(motif, length(s1)+1, ml);
			s3 = substr(motif, length(s2)+CONTEXT+1);
			if (length(s3) == 0) s3 = "X"
		}
	} else {
			s1 = substr(motif, 1, CONTEXT);
			s2 = substr(motif, length(s1)+1, ml);
			s3 = substr(motif, len-CONTEXT+1);
	}
	printf(" %d %d %s %s %s\n",pos,pos+ml,s1,s2,s3);
	
}
END {}
