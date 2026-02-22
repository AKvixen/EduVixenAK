# Smart Visual Assistant Debugging Guide

## Overview
This guide explains how to debug the Smart Visual Assistant image generation system using the comprehensive logging we've implemented.

## Debugging Steps

### 1. **Check Backend Console Logs**
When you generate a presentation, look for these specific log entries in the Replit console:

#### Step 1: Presentation Generator Input
```
🔍 [PRESENTATION] Calling Visual Assistant with: {
  context_text: "DNA Structure",
  keywords: "dna molecule biology",
  slide_number: 2
}
```
**What to check:** Verify the `context_text` and `keywords` are meaningful for image search.

#### Step 2: Visual Assistant Input Processing
```
🔍 [VISUAL ASSISTANT] Input received: {
  context_text: "DNA Structure",
  keywords: "dna molecule biology", 
  slide_number: 2,
  timestamp: "2025-07-26T10:30:00.000Z"
}
```
**What to check:** Confirm the Visual Assistant receives the correct input parameters.

#### Step 3: External API Call Construction
```
🔍 [UNSPLASH] Constructing API call: {
  originalContext: "DNA Structure",
  keywords: "dna molecule biology",
  searchQuery: "DNA Structure dna molecule biology",
  cleanQuery: "DNA Structure dna molecule biology",
  apiUrl: "https://api.unsplash.com/search/photos?query=DNA%20Structure%20dna%20molecule%20biology&per_page=10&orientation=landscape",
  timestamp: "2025-07-26T10:30:00.000Z"
}
```
**What to check:** Verify the search query makes sense and the API URL is properly formatted.

#### Step 4: External API Response
```
🔍 [UNSPLASH] API response status: {
  status: 200,
  statusText: "OK",
  ok: true,
  timestamp: "2025-07-26T10:30:00.000Z"
}
```
**What to check:** 
- Status should be `200` 
- `ok` should be `true`
- If status is `401`: API key is invalid
- If status is `403`: API key has no access/quota exceeded
- If status is `429`: Rate limit exceeded

#### Step 5: Raw API Response Data
```
🔍 [UNSPLASH] Raw API response: {
  totalResults: 1000,
  resultsCount: 10,
  firstResultTitle: "DNA double helix structure",
  firstResultUrl: "https://images.unsplash.com/photo-1559757148-5c350d0d3c56...",
  timestamp: "2025-07-26T10:30:00.000Z"
}
```
**What to check:**
- `totalResults` > 0 means images were found
- `resultsCount` > 0 means we got actual results
- `firstResultUrl` should be a valid Unsplash URL

#### Step 6: Selected Image Details
```
🔍 [UNSPLASH] Selected image details: {
  imageUrl: "https://images.unsplash.com/photo-1559757148-5c350d0d3c56...",
  photographer: "John Doe",
  description: "DNA double helix structure illustration",
  unsplash_id: "abc123def456",
  educationalImagesCount: 5,
  totalResults: 10,
  timestamp: "2025-07-26T10:30:00.000Z"
}
```
**What to check:** 
- Verify `imageUrl` is valid
- `educationalImagesCount` shows how many images passed the educational filter

#### Step 7: Visual Assistant Final Response
```
🔍 [VISUAL ASSISTANT] Final response to calling module: {
  imageFound: true,
  imageUrl: "https://images.unsplash.com/photo-1559757148-5c350d0d3c56...",
  attribution: "Photo by John Doe on Unsplash",
  hasMetadata: true,
  error: "none",
  timestamp: "2025-07-26T10:30:00.000Z"
}
```
**What to check:** 
- `imageFound` should be `true` for successful searches
- `imageUrl` should not be `null`
- `error` should be "none"

#### Step 8: Presentation Generator Response Processing
```
🔍 [PRESENTATION] Visual Assistant response: {
  slideTitle: "DNA Structure",
  imageFound: true,
  imageUrl: "https://images.unsplash.com/photo-1559757148-5c350d0d3c56...",
  hasAttribution: true,
  error: "none"
}
```

#### Step 9: Final Presentation Data
```
🔍 [PRESENTATION] Final presentation data summary: {
  totalSlides: 8,
  slidesWithImages: 3,
  slidesWithDiagrams: 5,
  imageUrls: [
    { title: "DNA Structure", url: "https://images.unsplash.com/photo-1559757148..." },
    { title: "Cell Division", url: "https://images.unsplash.com/photo-2234567890..." }
  ],
  timestamp: "2025-07-26T10:30:00.000Z"
}
```

### 2. **Check Frontend Console Logs**
Open Browser Developer Tools (F12) → Console Tab:

```
🔍 [FRONTEND] Received presentation data: {
  totalSlides: 8,
  slidesWithImages: 3,
  slidesWithDiagrams: 5,
  slideImageData: [
    {
      title: "DNA Structure",
      hasImage: true,
      imageUrl: "https://images.unsplash.com/photo-1559757148...",
      hasAttribution: true,
      hasDiagram: true
    }
  ]
}
```

### 3. **Check Network Tab**
In Browser Developer Tools → Network Tab:
1. Generate a presentation
2. Find the `/api/generate-presentation` request
3. Click on it → Response tab
4. Look for `imageUrl` fields in the slide objects

### 4. **Check Elements Tab**
In Browser Developer Tools → Elements Tab:
1. Find the slide with an image
2. Look for `<img>` tags
3. Check if `src` attribute has the correct URL
4. Look for broken image icons (🖼️❌)

### 5. **PPTX Export Debugging**
For PPTX export issues, check these logs:

```
🔍 [PPTX EXPORT] Export request received: {
  hasPresentation: true,
  slideCount: 8,
  slidesWithImages: 3,
  imageUrls: [
    { title: "DNA Structure", url: "https://images.unsplash.com/photo-1559757148..." }
  ],
  timestamp: "2025-07-26T10:30:00.000Z"
}
```

## Common Issues and Solutions

### Issue 1: No Images Found
**Symptoms:** `imageFound: false` in logs
**Check:** 
- Are the search terms educational/scientific?
- Is the Unsplash API key configured?
- Are there network connectivity issues?

### Issue 2: API Key Issues  
**Symptoms:** Status `401` or `403` in API response
**Solution:** Check `UNSPLASH_ACCESS_KEY` in Replit Secrets

### Issue 3: Images Don't Display in Frontend
**Symptoms:** Backend logs show images found, but frontend doesn't display them
**Check:**
- Browser console for JavaScript errors
- Network tab for failed image requests
- Elements tab for incorrect `src` attributes

### Issue 4: Images in App But Not in PPTX
**Symptoms:** Images display in web app but missing from exported PPTX
**Check:** PPTX export logs for image download and embedding process

## Environment Variables to Check
- `UNSPLASH_ACCESS_KEY`: Required for image search
- `NODE_ENV`: Should be "development" or "production"

## Quick Test Commands
```bash
# Test Visual Assistant endpoint directly
curl -X POST http://localhost:5000/api/visual-assistant/find-image \
  -H "Content-Type: application/json" \
  -d '{"context_text": "DNA structure", "keywords": "biology molecule"}'
```

This comprehensive logging system allows you to trace the complete flow from presentation generation through image search to final display, making it easy to identify exactly where any issues occur.