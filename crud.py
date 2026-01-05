from sqlalchemy.orm import Session
from sqlalchemy import text

def fts_search(db: Session, query: str, limit: int = 40):
    """
    Perform PostgreSQL FTS search using prefix matching.
    """
    if not query.strip():
        return []

    # Sanitize input & add :* for prefix search
    ts_query = ' & '.join(word + ':*' for word in query.split())

    sql = text(f"""
        SELECT page_title, navigated_to_url
        FROM browsing_history
        WHERE search_vector @@ to_tsquery('english', :ts_query)
        ORDER BY ts_rank_cd(search_vector, to_tsquery('english', :ts_query)) DESC
        LIMIT :limit
    """)
    result = db.execute(sql, {"ts_query": ts_query, "limit": limit})
    return result.fetchall()
