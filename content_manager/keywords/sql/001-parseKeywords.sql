CREATE OR REPLACE FUNCTION content_manager_keywords_parsestr(INPUT_STR text) RETURNS text AS $keywords_parsestr$
DECLARE
    KEYWORD content_manager_keywords_keyword%rowtype;
    MESSAGE_STRING text[];
    OUTPUT_STR text;
    MSG text;
    SLUGGED text;
    POSMARK int;
    MSGCOUNT int;
BEGIN
    MESSAGE_STRING := string_to_array(INPUT_STR,' ');
    MSGCOUNT = 1;
    FOREACH MSG IN ARRAY MESSAGE_STRING
  LOOP
   POSMARK := position('#' in MSG);
   IF POSMARK = 1 THEN
        SLUGGED := slugify(MSG);
        SELECT * INTO KEYWORD FROM content_manager_keywords_keyword WHERE hash = SLUGGED;
        IF NOT FOUND THEN
            INSERT INTO content_manager_keywords_keyword (hash,keyword,created,updated,items,views,likes,dislikes,shares,comments,active,archived,hidden) VALUES (SLUGGED,MSG,current_timestamp,current_timestamp,0,0,0,0,0,0,true,false,false);
            SELECT * INTO KEYWORD FROM content_manager_keywords_keyword WHERE hash = SLUGGED;
        END IF;
        UPDATE content_manager_keywords_keyword SET items = items + 1, UPDATED = current_timestamp WHERE id = KEYWORD.id;
        MESSAGE_STRING[MSGCOUNT] := '<a class="link pill keyword" target="_blank" href="/s/k/'||SLUGGED||'">'||MSG||'</a>';
   END IF;
   MSGCOUNT := MSGCOUNT +1;
  END LOOP;
    OUTPUT_STR := array_to_string(MESSAGE_STRING,' ');
    RETURN OUTPUT_STR;
END;
$keywords_parsestr$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION content_manager_get_str_keyword_ids(INPUT_STR text) RETURNS int[] AS $get_str_keyword_ids$
DECLARE
    KEYWORD content_manager_keywords_keyword%rowtype;
    MESSAGE_STRING text[];
    KEYWORD_IDS int[];
    OUTPUT_STR text;
    MSG text;
    SLUGGED text;
    POSMARK int;

BEGIN
    MESSAGE_STRING := string_to_array(INPUT_STR,' ');
    FOREACH MSG IN ARRAY MESSAGE_STRING
  LOOP
   POSMARK := position('#' in MSG);
   IF POSMARK = 1 THEN
        SLUGGED := slugify(MSG);
        SELECT * INTO KEYWORD FROM content_manager_keywords_keyword WHERE hash = SLUGGED;
        IF NOT FOUND THEN
            INSERT INTO content_manager_keywords_keyword (hash,keyword,created,updated,items,views,likes,dislikes,shares,comments,active,archived,hidden) VALUES (SLUGGED,MSG,current_timestamp,current_timestamp,0,0,0,0,0,0,true,false,false);
            SELECT * INTO KEYWORD FROM content_manager_keywords_keyword WHERE hash = SLUGGED;
            UPDATE content_manager_keywords_keyword SET items = items + 1, UPDATED = current_timestamp WHERE id = KEYWORD.id;
        END IF;
        KEYWORD_IDS = array_append(KEYWORD_IDS,KEYWORD.id);
   END IF;

  END LOOP;
    RETURN KEYWORD_IDS;
END;
$get_str_keyword_ids$ LANGUAGE plpgsql;
