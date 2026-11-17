// src/types/feature.ts
export interface ClothingItem {
  id: string;
  name: string;
  category: 'tops' | 'bottoms' | 'outerwear' | 'footwear' | 'accessories';
  weather: 'sunny' | 'rainy' | 'cold' | 'hot' | 'mild' | 'snowy';
  style: 'casual' | 'formal' | 'sporty' | 'business' | 'party';
  imageUrl?: string;
}

export interface OutfitSuggestion {
  id: string;
  title: string;
  description: string;
  items: ClothingItem[];
  weather: string;
  style: string;
  rating?: number;
}

export interface OutfitFilterState {
  weather: 'sunny' | 'rainy' | 'cold' | 'hot' | 'mild' | 'snowy' | 'all';
  style: 'casual' | 'formal' | 'sporty' | 'business' | 'party' | 'all';
}
